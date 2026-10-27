# CLAUDE.md

Orientação para agentes de código trabalhando neste repo.

## O que é este repo

Site oficial da **Arraial Expo XP** (Feira de Ciência e Tecnologia de Arraial do Cabo, Prefeitura/PMAC): produção em **expoxp.arraial.rj.gov.br** = Worker `expoxp` da Cloudflare. Fonte única desde 27/10/2026 (não existe mais pasta-fonte espelhada). Edição 2026: tema **Mulheres na Ciência**, feira em **3 e 4 de novembro de 2026** (local ainda não anunciado).

Documentação viva: `README.md` (como editar/publicar), `PLANO-2026.md` (pipeline dos jogos), `MULHERES-NA-CIENCIA.md` (dossiê das cientistas citadas).

## Estrutura

```
index.html        # home 2026 (autocontida)
edicoes.html      # edições 2023/2025 (só existe aqui)
jogos/            # portal + Duelo de Laboratório + Diário de Cientista
audio/nomes/      # MP3s de pronúncia 🔊 (idioma original de cada nome)
ferramentas/      # gerador de áudio (gTTS) — não sobe no deploy
docs/, test/      # material interno — não sobe no deploy
```

## Regras da casa

- **Página = arquivo HTML único autocontido** (CSS/JS inline, zero dependências, zero build, conteúdo PT-BR). Não introduzir bundlers, frameworks nem assets externos sem discussão.
- **Linguagem neutra para quem joga** — nunca genderizar jogadoras/jogadores; as cientistas do conteúdo podem (e devem) ser mulheres.
- **O hub `/jogos` só lista jogo publicado** — nunca card "em breve".
- **Pronúncia 🔊**: todo nome de cientista citado em UI tem MP3 em `audio/nomes/` + entrada no mapa `PRONUNCIAS` da página (`a` = slug do arquivo, `v` = idioma BCP-47, `f` = texto do fallback Web Speech). Gerar/alterar áudio: `python3 ferramentas/gerar_audio_nomes.py [--forca]` (requer `pip install --user --break-system-packages gTTS`).
- **QA interno**: modo `?gabarito` escondido nas páginas de jogo (duelo marca a correta; diário reproduz sozinho + roteiro completo).
- **Lições já pagas**: timer por JS (transição CSS não arranca de `display:none`); contêineres animados sempre `display:block`/`flex`; timer de segurança em APIs de fala que não disparam eventos.

## Deploy

`git push origin master` + **deploy direto** (Workers Builds quebrado desde jul/2026 — ver README §Publicar):

```bash
T=$(grep -m1 '^export CLOUDFLARE_API_TOKEN=' ~/.zshrc | cut -d= -f2- | tr -d '"')
CLOUDFLARE_API_TOKEN="$T" wrangler deploy
```

`.assetsignore` exclui do worker tudo que não é site (`*.md`, `docs`, `ferramentas`, `test`…). O worker serve `/x.html` como `/x` (redirect 307).
