# ExpoXP 2026 — Plano A (inovação) + Plano B (fallback)

**Edição:** 3ª · **Tema:** Mulheres na Ciência · **Período provável:** novembro de 2026 *(datas a confirmar)*
**Decisão (22/10/2026):** Plano A = identidade "Laboratório Vivo" + jogos de mecânicas novas, construídos **em ordem de custo, do baixo pro alto**, publicando cada um assim que pronto. Plano B (reaproveitamento dos padrões de 2025) fica documentado como fallback se a semana apertar.

---

## PLANO A — Laboratório Vivo

### 1. Identidade visual 2026: "Laboratório Vivo"

O que **sai**: bolhas orgânicas, formas aquáticas, gradientes verde-água (eco de "Planeta Água" 2025) e o violeta provisório do esquenta.

O que **entra**:

| Elemento | Especificação |
|---|---|
| Fundo claro | Papel frio (#F7FAFC) com **rede de hexágonos sutil** (traço azul a ~5%) |
| Fundo escuro | Azul quase preto (#0B1420) com hexágonos a brilhar em verde-lima fraco |
| Cor de interação | Azul profundo da marca (#01579B → hover #0288D1); no escuro, **verde-lima #AEEA00** com texto escuro (o "brilho do laboratório") |
| Acento decorativo | Verde-lima em bordas, glows e ligações químicas — nunca como texto sobre fundo claro (contraste) |
| Decoração | Vidraria em **line-art SVG** (erlenmeyer, tubos de ensaio) e **moléculas animadas** (clusters de hexágonos ligados por linhas) |
| Formas | Hexágonos e linhas de ligação — nada de círculos orgânicos flutuantes |
| Tipografia | Inalterada (pilha da casa) |

**Por que funciona:** o tema é "Mulheres na **Ciência**" — o laboratório é o lugar comum de todas elas (da química de Marie Curie ao "laboratório" que é um navio de oceanografia do IEAPM). A rede de ligações também é a metáfora dos jogos: nada nasce sozinho, ciência é conexão.

**Aplicação imediata:** o esquenta já é re-skinado com essa identidade (bolhas → hexágonos + vidraria).

### 2. Os jogos do Plano A — pipeline por custo

Regra de ouro herdada de 2025: **o hub só lista jogo publicado**. Nada de card "Em breve" — se o prazo apertar, o jogo que não terminou simplesmente não entra (e pode entrar depois do evento).

---

#### Jogo 1 — Duelo de Laboratório *(hotseat · custo baixo · ~1-2 dias)* — ✅ **PUBLICADO em 22/10/2026** (`expoxp.arraial.rj.gov.br/jogos`)

- **Motivação:** ciência como duelo — competição saudável na Arena Gamer, pai×filho, amigo×amigo. O conhecimento vira festa, não prova.
- **Mecânica:** 2 jogadores **no mesmo aparelho**, alternando a vez ("passe o celular"). 3 rodadas temáticas (Quem foi ela? / Feito → cientista / Mito ou ciência), cada acerto enche o **tubo de ensaio do jogador** (placar visual). Rodada final "reação rápida": timer decrescente valendo duplo. Vencedor recebe um título de cientista ("Dra. Duelo" etc.).
- **Diferença de 2025:** multiplayer social, pressão de tempo, placar vivo — 2025 era single-player sem relógio.
- **Conteúdo necessário:** banco de ~30 perguntas (reaproveita o quiz do esquenta + plano B).
- **Pronto quando:** 2 jogadores completam uma partida no celular; empate resolvido; perguntas revisadas.

#### Jogo 2 — Diário de Cientista *(narrativa ramificada · custo baixo-médio · ~2-3 dias)* — ✅ **PUBLICADO em 22/10/2026** (`expoxp.arraial.rj.gov.br/jogos/diario`) · *roteiro escrito pela CETEC com apoio de IA — pendente de revisão docente; ajustes de texto são triviais (dados num único objeto `NODES`)*

- **Motivação:** **representatividade como mecânica** — a jogadora é uma menina de Arraial do Cabo decidindo seu caminho; cada escolha mostra consequência real. O jogo responde à pergunta que o tema levanta: "e se fosse eu?".
- **Mecânica:** ficção interativa (estilo twine, JS puro, zero dependência): capítulos com 2-3 escolhas, flags que mudam o texto seguinte, **3 finais-carreira** (oceanógrafa no IEAPM / engenheira / cientista da computação) + epílogo "o que essa carreira faz aqui na cidade". Tela final "meu diário" mostra o percurso escolhido; convida ao replay nos outros caminhos.
- **Diferença de 2025:** zero perguntas e respostas; é jogo de escolha e consequência, com conteúdo **local**.
- **Conteúdo necessário:** roteiro de ~40-60 nós (a parte caro é texto, não código) + revisão pedagógica.
- **Pronto quando:** 3 finais alcançáveis; leitura fluída no celular; nomes/locais de Arraial corretos.

#### Jogo 3 — Ligações da Ciência *(grafo de descoberta · custo médio · ~3-4 dias)*

- **Motivação:** a história da ciência é uma **rede** — nenhuma descoberta nasce sozinha. O prazer de completar o mapa ("reação completa").
- **Mecânica:** tabuleiro em SVG/canvas com 12-15 cientistas como **nós de uma rede molecular**; arestas ocultas. O jogador propõe ligações (cientista ↔ feito / cientista ↔ quem inspirou); correta = **linha acende em verde-lima** + micro-história; errada = dica educativa. 3 mapas: Brasil → Mundo → Nossas cientistas (local). Completar o mapa dispara animação de "reação em cadeia" iluminando tudo.
- **Diferença de 2025:** descoberta livre em grafo, sem pergunta com opções fixas; exploração em vez de resposta.
- **Conteúdo necessário:** curadoria das ligações (biografias verificáveis) — o mesmo material do Mural/quiz serve de base.
- **Pronto quando:** 3 mapas jogáveis; toque funciona no celular; texto das dicas revisado.
- *Obs.: é a "Constelação" aprovada na conversa, re-vestida de rede molecular pra casar com o Laboratório Vivo.*
- **Execução (27/10/2026): PUBLICADO** — `/jogos/ligacoes` com 20 ligações em 3 mapas (Ciência do Brasil → Rede Mundial → Estrelas e Oceanos). O 3º mapa é da laia do acervo curado; o mapa "Nossas cientistas (local)" foi adiado até haver curadoria local — entra como 4º mapa sem quebrar nada. Modo `?gabarito` (fios tracejados + botão que abre o **grafo completo** sem jogar) e 🔊 de pronúncia nos chips. Pós-revisão (27/10): colunas embaralhadas a cada partida (as donas nasciam alinhadas às respostas), tela "A rede completa" com os 3 mapas ao fim do jogo, e **ordem de apresentação do portal ajustada por dificuldade**: Ligações (1º) → Diário (2º) → Ada (3º) → Duelo (último, 27/10).

#### Jogo 4 (stretch) — Código de Ada *(programação visual · custo médio-alto · ~4-5 dias)*

- **Motivação:** "eu mando no computador" — agência sobre tecnologia, homenagem à primeira programadora da história.
- **Mecânica:** grade 8×8, um rover coletor de amostras; o jogador monta programas com **blocos visuais** (avançar, girar ⟲⟳, repetir N×) que executam animados; 8-10 níveis com obstáculos (estantes, microscópios) e amostras; estrelas por eficiência (menos blocos).
- **Diferença de 2025:** construção de solução (programar), não seleção de resposta.
- **Gatilho:** só começa se os 3 primeiros estiverem publicados **até ~02/nov**. Senão, vira pós-evento ou 2027.
- *Execução (27/10/2026): **PUBLICADO** — `/jogos/ada`* com 8 níveis (avançar → girar → laços → serpentina → diagonal), estrelas por eficiência (≤ par = 3★), laço `REPETIR N×` de um nível (sem aninhamento), memos de laboratório por nível com os fatos já curados (Ada, Grace, Hedy, Katherine, Mayana, Bertha, Marie, Dorothy) e 🔊 de pronúncia, progresso em `localStorage`, modo `?gabarito` (badge + botão que carrega a solução ideal).

#### Jogo-bandeira da feira — Guardiãs da Ciência *(externo · fora do pipeline)*

- **Execução (29/10/2026): integrado ao portal e à home.** Jogo maior construído à parte (Claude artifact) e publicado em domínio próprio: **`guardioes-expo.arraial.rio.br`** — "A manhã sem nomes": cerração apaga os nomes das 22 cientistas espalhadas pelos locais reais de Arraial; o jogador as encontra, refaz as descobertas e devolve os nomes. Contas por apelido (sem senha/e-mail), salvamento por QR code/código de 6 letras, mapa OpenStreetMap, pixel art, chat só com frases prontas até um adulto guardar a conta.
- No portal (`/jogos`) e na seção Jogos da home entra como **card de destaque no topo** (🧭, borda e selo "★ O grande jogo da feira") — link externo direto, sem iframe. A ordem pedagógica dos 4 jogos nativos permanece: Ligações → Diário → Ada → Duelo.

#### Sugestões extras (pedidas na conversa — não estão no pipeline)

- **Mastermind das Cientistas** *(dedução · custo baixo)*: adivinhe a cientista secreta por atributos (século/área/país) com feedback lógico estilo Mastermind/Guess Who. Mecânica dedutiva inédita; cabe como 4º barato se Ada cair.
- **Reação em Cadeia** *(puzzle físico · custo médio-alto)*: posicione catalisadores no cenário, dispare e veja a reação propagar (Rube Goldberg químico). Bonito com o tema, melhor deixar pós-evento.

### 3. Cronograma (hoje = 22/out · evento ~05-14/nov a confirmar)

| Quando | Entrega | Status |
|---|---|---|
| 22–23/out | Re-skin do esquenta (Laboratório Vivo) + publicação do esquenta | ✅ feito (22/out) |
| 22–26/out | **Duelo de Laboratório** no ar | ✅ feito (22/out, `/jogos`) |
| 27–29/out | **Diário de Cientista** no ar | ✅ feito (22/out, `/jogos/diario`) |
| 30/out–02/nov | **Ligações da Ciência** no ar | ✅ feito (27/out, `/jogos/ligacoes`) |
| 03/nov+ | **Código de Ada** — só se os 3 acima estiverem publicados | ✅ feito (27/out, `/jogos/ada`) |
| 29/out | **Guardiãs da Ciência** (externa) no portal e na home como destaque | ✅ feito (29/out, card destaque) |
| semana do evento | Arena Gamer usa o portal; banner no site oficial | — |

*Nota de infra (22/out): o portal está publicando dentro do worker `expoxp` em `/jogos/` (deploy direto com wrangler; builds do git seguem quebrados). O repo/CNAME dedicado `jogosdaciencia.arraial.rj.gov.br` fica como migração futura quando o dash for consertado.*

Cada jogo entra no ar no dia em que termina (deploy é push). Se qualquer data deslizar 1-2 dias, cai o jogo seguinte — nunca a qualidade do que já saiu.

### 4. Assunptions a validar (o que pode derrubar o plano)

- [ ] **Datas oficiais** — se o evento for na 1ª semana de novembro, Ada nasce pós-evento por definição.
- [ ] **Roteiro do Diário** — sem revisão pedagógica a tempo, o jogo perde a graça; validador: primeira leitura de um professor.
- [ ] **Curadoria das ligações** — o jogo 3 depende de biografias verificáveis (nada de "fact" inventado); validador: checagem por 2 fontes.
- [ ] **Público no celular** — Arena tem telões, mas o público volta pro celular; tudo nasce mobile-first.

### 5. Not Doing (e por quê)

- **Álbum/meta-colecionável** — escolhido "3 jogos sem meta"; camada meta fica como ideia pra 2027.
- **Multiplayer online real** — exigiria servidor; hotseat resolve 90% da graça com 0 infra.
- **Áudio/narração** — custo de gravação e licença; texto bem escrito entrega primeiro. *(Exceção adotada em 26/10/2026: a **pronúncia dos nomes** 🔊 usa MP3s curtos gerados por gTTS — `ferramentas/gerar_audio_nomes.py` + `audio/nomes/` — custo zero, sem licença, presentes na home e nos jogos. Narração de textos continua fora.)*
- **Fotos reais das cientistas nos jogos** — licenciamento lento; line-art/emoji agora, fotos no Mural do site oficial depois.

---

## PLANO B — fallback rápido (se a semana desandar)

Aprovação das mecânicas de 2025 com roupagem nova + conteúdo 2026. **Pronto rapidamente porque reusa templates existentes:**

| # | Jogo | Base reutilizável | Conteúdo novo |
|---|---|---|---|
| 1 | Quem é ela? (estendido) | `QuizInterativo.html` | ~15-20 perguntas (o quiz do esquenta já é a semente) |
| 2 | Mito ou Ciência? | `EscolhaCertaOuErrada.html` | ~15 afirmações com fonte |
| 3 | Monte o Laboratório | `ArrastarESoltar.html` | pares área↔símbolo↔cientista |

**Gatilho de troca A→B:** se até 27/out não houver nenhum jogo do Plano A publicado, migra pro B — o evento não pode ficar sem portal.

Também preservado do planejamento anterior: **Mural das Cientistas** (contribuição das escolas → cards no site oficial), que roda independente de A ou B e ataca a dor de "falta de contribuição de participantes".

---

## Infra (comum a A e B)

- Repo novo `pmaccetec/jogosdaciencia`, CNAME `jogosdaciencia.arraial.rj.gov.br`, integração git Cloudflare, **um HTML autocontido por jogo + hub** — padrão da casa, sem build/servidor.
- **Esquenta (22/10/2026): publicado no repo oficial via opção B** (`esquenta2026.html` + banner/menu/CTA na home; sem formulário — o cadastro volta com o Plano A). Aguardando o build do Cloudflare voltar a funcionar: os *Workers Builds* do projeto `expoxp` falham instantâneo desde ~out/2026 (último build bom: 17/jul/2026) — runbook de desbloqueio no README do esquenta.
- Formulário: desativado até o Plano A (decisão da equipe em 22/10/2026); quando voltar, preferir backend real (Worker/Google Forms) em vez de front-only.

## Métricas

Views do portal e do esquenta (analytics Cloudflare), partidas iniciadas/concluídas por jogo (contador simples), cadastros recebidos, e nº de escolas no Mural.
