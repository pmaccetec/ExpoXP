# Expo XP — site oficial (repo único)

Produção: **expoxp.arraial.rj.gov.br** = Worker `expoxp` da Cloudflare (repo GitHub `pmaccetec/ExpoXP`, branch `master`).

Desde **27/10/2026 este repo é a fonte única** do site: a antiga pasta-fonte espelhada (`~/Cetec/mulheres-na-ciencia`) foi **eliminada** — edita aqui mesmo e publica daqui. Não existe mais etapa de cópia.

Padrão da casa: **páginas HTML únicas autocontidas** (CSS/JS inline), zero dependências, zero build, conteúdo em PT-BR.

- **Identidade 2026 — "Laboratório Vivo":** azul profundo + verde-lima `#AEEA00`, papel quadriculado, hexágonos/moléculas, vidraria em line-art SVG.
- **Jogos da edição e pipeline:** [PLANO-2026.md](PLANO-2026.md).
- **Dossiê das cientistas citadas (história e relevância):** [MULHERES-NA-CIENCIA.md](MULHERES-NA-CIENCIA.md).

## Rodar localmente

```bash
python3 -m http.server 8000   # ou a porta que estiver usando (ex.: 8123)
```

Abrir `http://localhost:8000`. Não há build, `package.json` nem dependências.

## O que tem no site

| Rota | Conteúdo |
|---|---|
| `/` | Home 2026 "Mulheres na Ciência": hero + contagem regressiva (**feira: 3 e 4/11/2026**), tema+estatísticas, 12 cards de cientistas com 🔊 pronúncia, seção Jogos, edições anteriores |
| `/edicoes` | Site das edições 2023/2025 (histórico, sem newsletter; ponte de volta pro 2026) |
| `/jogos` | Portal Jogos da Ciência: **Guardiãs da Ciência** em card de destaque no topo (jogo-bandeira da feira, externo — `guardioes-expo.arraial.rio.br`, mapa de Arraial com 22 cientistas, contas por apelido) e, em ordem pedagógica (do mais fácil pro mais difícil): **Ligações da Ciência** (rede de descobertas, 3 mapas + grafo completo no fim) → **Diário de Cientista** (narrativa interativa, 3 finais) → **Código de Ada** (programação visual, 8 níveis) → **Duelo de Laboratório** (hotseat 2 jogadores) — o hub só lista jogo publicado, nunca "em breve" |
| `/audio/nomes/` | MP3s de pronúncia 🔊 dos nomes das cientistas (no idioma original de cada uma) — usados por home e jogos |

## Onde editar as coisas importantes

- **Data da contagem regressiva:** constante `DATA_ALVO_COUNTDOWN` no `<script>` do `index.html` (hoje 3/nov/2026, 1º dia da feira) e os rótulos "Contagem regressiva para…" / notinha do local. O **local da feira ainda não foi anunciado**.
- **Perguntas do Duelo:** array `BANK` no script do `jogos/duelo.html`.
- **Mapas do Ligações:** array `MAPAS` no script do `jogos/ligacoes.html` (cientistas ↔ descobertas, dica e micro-história por ligação).
- **História do Diário:** objeto `NODES` no script do `jogos/diario.html` (datas do prólogo seguem "Novembro de 2026" sem dia).
- **Cards de cientistas:** seção `#cientistas` do `index.html` — cada card é um `<button class="flip-card">` dentro de um `.flip-wrap` (que também abriga o botão 🔊).
- **Pronúncia dos nomes (🔊):** MP3s de `audio/nomes/` gerados por `python3 ferramentas/gerar_audio_nomes.py` (gTTS, `--forca` regenera tudo). Cada página tem seu mapa `PRONUNCIAS` (nome → arquivo + texto/idioma do fallback). Trocou/adicionou cientista? Gere o áudio, atualize o(s) mapa(s) e o dossiê `MULHERES-NA-CIENCIA.md`.
- **Cores da edição:** tokens `--lab-*` no `:root` do `index.html`.
- **Tema claro/escuro:** chave de `localStorage` `expo-xp-theme` (compartilhada com o site das edições).

## Publicar

```bash
git add . && git commit -m "..." && git push origin master
```

Os *Workers Builds* (auto-deploy por push) **falham instantaneamente desde jul/2026** — causa na configuração do projeto no Cloudflare, não no repo. Enquanto isso, **publicar = deploy direto**:

```bash
cd ~/Cetec/expo-xp
T=$(grep -m1 '^export CLOUDFLARE_API_TOKEN=' ~/.zshrc | cut -d= -f2- | tr -d '"')
CLOUDFLARE_API_TOKEN="$T" wrangler deploy
```

Pra consertar o auto-deploy de vez: abrir o último build no dash (`dash.cloudflare.com/…/workers/services/view/expoxp/production/builds`) e ler o erro — provável reconexão do repo em *Settings → Build*. Obs: `wrangler login` (OAuth) só funciona depois de `unset CLOUDFLARE_API_TOKEN`.

`.assetsignore` garante que só conteúdo do site sobe no worker (docs, `*.md`, `ferramentas/`, `test/` ficam de fora).

## Pendências conhecidas

- [ ] Anunciar o **local** da feira (notinha da home + nó `abertura` do Diário na mesma leva).
- [ ] Formulário de notificações sem backend — integrar Google Forms ou Worker (PLANO-2026 §5).
- [ ] Substituir emojis dos cards por fotos licenciadas das cientistas (padrão Cloudinary).
- [ ] Migrar o quiz como "modo solo" do portal `/jogos`.
