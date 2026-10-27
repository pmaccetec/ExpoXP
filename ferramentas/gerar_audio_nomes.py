#!/usr/bin/env python3
"""Gera os MP3 de pronúncia dos nomes das cientistas em audio/nomes/.

Cada nome é falado NA LÍNGUA ORIGINAL da cientista (Marie Curie em francês,
Katherine Johnson em inglês, Johanna Döbereiner em alemão...) — as
brasileiras ficam em pt-BR. Vozes do gTTS (Google), arquivos estáticos: o
site continua sem servidor e sem dependência em runtime.

Rodar quando adicionar/trocar cientista (ou ajustar idioma/texto):

    python3 ferramentas/gerar_audio_nomes.py            # só o que falta
    python3 ferramentas/gerar_audio_nomes.py --forca    # regenera tudo

Depois, atualize o mapa PRONUNCIAS da página onde o nome aparece
(index.html, jogos/duelo.html, jogos/diario.html): "f" é o texto do
fallback (Web Speech API, caso o MP3 não carregue) e "v" é o idioma
BCP-47 dessa fala. No deploy, a pasta audio/ vai junto (cópia idêntica
pro repo oficial, como jogos/).
"""
import pathlib
import subprocess
import sys
import unicodedata

from gtts import gTTS

RAIZ = pathlib.Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "audio" / "nomes"

# nome exibido no site → (idioma gTTS, texto falado)
# (o nome do arquivo .mp3 é o slug do nome exibido)
NOMES = {
    # — os 12 cards da home (que também aparecem no Duelo) —
    "Marie Curie":               ("fr", "Marie Curie"),
    "Ada Lovelace":              ("en", "Ada Lovelace"),
    "Katherine Johnson":         ("en", "Katherine Johnson"),
    "Rosalind Franklin":         ("en", "Rosalind Franklin"),
    "Bertha Lutz":               ("pt-br", "Bertha Lutz"),
    "Johanna Döbereiner":        ("de", "Johanna Döbereiner"),
    "Nise da Silveira":          ("pt-br", "Nise da Silveira"),
    "Enedina Alves Marques":     ("pt-br", "Enedina Alves Marques"),
    "Mayana Zatz":               ("pt-br", "Mayana Zatz"),
    "Jaqueline Goes":            ("pt-br", "Jaqueline Goes"),
    "Hedy Lamarr":               ("de", "Hedy Lamarr"),
    "Mae Jemison":               ("en", "Mae Jemison"),
    # — só no Duelo —
    "Dorothy Hodgkin":           ("en", "Dorothy Hodgkin"),
    "Grace Hopper":              ("en", "Grace Hopper"),
    "Chien-Shiung Wu":           ("zh-cn", "吴健雄"),  # Wu Jianxiong
    "Vera Rubin":                ("en", "Vera Rubin"),
    "Sally Ride":                ("en", "Sally Ride"),
    "Valentina Tereshkova":      ("ru", "Валентина Терешкова"),
    "Sylvia Earle":              ("en", "Sylvia Earle"),
    # — duplas de mesmo idioma (texto exato da alternativa do Duelo) —
    "Marie Curie e Irène Joliot-Curie":       ("fr", "Marie Curie et Irène Joliot-Curie"),
    "Ada Lovelace e Grace Hopper":            ("en", "Ada Lovelace and Grace Hopper"),
    "Rosalind Franklin e Dorothy Hodgkin":    ("en", "Rosalind Franklin and Dorothy Hodgkin"),
}

# duplas com idiomas mistos: geradas em partes e emendadas com ffmpeg
DUPLAS_MISTAS = {
    "Emmanuelle Charpentier e Jennifer Doudna": [
        ("fr", "Emmanuelle Charpentier"),
        ("en", "Jennifer Doudna"),
    ],
}


def slug(nome: str) -> str:
    normalizado = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode()
    partes = [p for p in normalizado.lower().replace("-", " ").split() if p]
    return "-".join(partes)


def emendar(partes, alvo: pathlib.Path) -> None:
    """Concatena os MP3s das partes com 0,35s de respiro entre elas."""
    entradas = []
    arquivos = []
    for i, (idioma, texto) in enumerate(partes):
        parte = alvo.with_suffix(f".parte{i}.mp3")
        gTTS(texto, lang=idioma).save(str(parte))
        arquivos.append(parte)
        entradas.append(f"[{i}:a]")
    filtro = "[0:a]apad=pad_dur=0.35[p0];[p0]" + "".join(entradas[1:]) + \
             f"concat=n={len(partes)}:v=0:a=1"
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error",
         *[arg for a in arquivos for arg in ("-i", str(a))],
         "-filter_complex", filtro, str(alvo)],
        check=True,
    )
    for parte in arquivos:
        parte.unlink()


def main() -> None:
    forcar = "--forca" in sys.argv
    DESTINO.mkdir(parents=True, exist_ok=True)

    gerados, pulados = [], []

    def gera(nome, alvo, *args):
        if alvo.exists() and not forcar:
            pulados.append(alvo.name)
            return
        if nome in DUPLAS_MISTAS:
            emendar(DUPLAS_MISTAS[nome], alvo)
        else:
            idioma, texto = args
            gTTS(texto, lang=idioma).save(str(alvo))
        gerados.append(alvo.name)

    for nome, (idioma, texto) in NOMES.items():
        gera(nome, DESTINO / f"{slug(nome)}.mp3", idioma, texto)
    for nome in DUPLAS_MISTAS:
        gera(nome, DESTINO / f"{slug(nome)}.mp3")

    for lista, rotulo in ((gerados, "gerados"), (pulados, "já existentes")):
        if lista:
            print(f"{len(lista)} {rotulo}: {', '.join(sorted(lista))}")


if __name__ == "__main__":
    main()
