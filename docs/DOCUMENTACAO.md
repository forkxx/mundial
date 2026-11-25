# Forkão no Raraland — Documentação do projeto

Site para divulgar e arrecadar fundos para o Forkxx ir ao Mundial de Warcraft 3 (Being Esports World Series 2027), um evento feito pela comunidade.

- Repositório: github.com/forkxx/mundial (vazio até aqui)
- Referência visual e técnica: Mídia Kit em forkxx.github.io (repo forkxx/forkxx.github.io)
- Mockup: https://claude.ai/artifact/LdNjUTZigbaaJUCAkabW5g

## 1. Objetivo

1. Hypar a comunidade de Warcraft 3 para o evento.
2. Arrecadar R$ 11.000,00 até 11/02/2027.
3. Dar transparência: quanto falta, para onde vai o dinheiro, quem apoiou.
4. Ser a página única para todos os links de doação (Pix, PayPal, lives).

## 2. Fatos do projeto (fonte: planilha "FORKÃO NO RARALAND")

| Item | Valor |
|---|---|
| Meta total | R$ 11.000,00 |
| Viagem | R$ 7.500,00 |
| Hospedagem | R$ 2.500,00 |
| Uber e afins | R$ 500,00 |
| Comida / fundo reserva | R$ 500,00 |
| Arrecadado (hoje) | R$ 0,00 |
| Data máxima de arrecadação | 11/02/2027 |
| Evento | Scholl Hundisburg, Alemanha, 11 a 14/03/2027 |
| Info do evento | liquipedia.net/warcraft/Being_Esports_World_Series/2027 |

Como ajudar:
- PIX com mensagem na live (QR Code da Midpix/Midfielder) e PIX direto (chave aleatória 98547923-1f68-4439-820b-a2eac65629ed)
- PayPal: max_lp_rox@hotmail.com

Regras de negócio (FAQ da planilha):
- Meta não atingida no prazo: campeonato brasileiro de Warcraft 3 com 100% do arrecadado.
- Sobra de dinheiro após a cobertura: também vira campeonato com o valor restante.
- O prazo é 1 mês antes do evento para comprar passagens e reservas sem preço abusivo.
- Conteúdo no evento: vlogs diários (YouTube, TikTok, Instagram), transmissão na Twitch com VODs no YouTube, entrevistas, showmatches e gameplays com a galera do War3.

Pendências de dados: o Excel original não chegou, só o PDF. As abas de apoiadores estão vazias no PDF. Se houver outras abas ou dados no Excel, enviar.

## 3. Estrutura do site (one-page)

1. Navegação fixa: Meta, Como ajudar, O evento, Apoiadores, Dúvidas, botão Apoiar.
2. Hero: título, chamada, datas, CTAs, foto.
3. Meta: valor arrecadado, barra de progresso, percentual, prazo, detalhamento dos 4 custos, contagem regressiva.
4. Como ajudar: três cartões com ícone: PIX (com mensagem na live: QR + botão para a Midpix), PIX direto (chave + botão copiar) e PayPal. O cartão de doações nas lives foi removido.
5. O evento: local, data, link Liquipedia, o que será produzido.
6. Apoiadores: tabela Nome, Data, Valor (estado vazio com convite).
7. Dúvidas: FAQ.
8. Rodapé: link para o Mídia Kit.

## 4. Stack e arquitetura

Mesma abordagem do Mídia Kit: site estático, sem build, hospedado no GitHub Pages.

- `index.html` único (HTML + CSS + JS embutidos), `en.html` para a versão em inglês (fase 2).
- `data.json` com meta, arrecadado, prazo e apoiadores. O JS lê o arquivo e preenche a página. Atualizar o site = editar `data.json` e fazer commit.
- `assets/` com imagens em .webp, favicon, imagem Open Graph, QR do Pix.
- `.nojekyll` na raiz.
- Fontes: Baloo 2 (títulos) e Inter (texto) via Google Fonts.
- Sem backend. Nenhum dado de pagamento passa pelo site: ele só exibe a chave Pix, o e-mail do PayPal e links.

Estrutura do repo:

```
mundial/
├── index.html
├── en.html            (fase 2)
├── data.json
├── .nojekyll
├── README.md
├── docs/DOCUMENTACAO.md
└── assets/
    ├── favicon.png, apple-touch-icon.png, og.png
    ├── pix-qr.webp
    └── foto-forkxx.webp
```

Exemplo de `data.json`:

```json
{
  "meta": 11000,
  "arrecadado": 0,
  "prazo": "2027-02-11",
  "evento": { "inicio": "2027-03-11", "fim": "2027-03-14" },
  "custos": [
    { "nome": "Viagem", "valor": 7500 },
    { "nome": "Hospedagem", "valor": 2500 },
    { "nome": "Uber e afins", "valor": 500 },
    { "nome": "Comida / fundo reserva", "valor": 500 }
  ],
  "apoiadores": [
    { "nome": "Apelido", "data": "2026-12-01", "valor": 50 }
  ]
}
```

O total "arrecadado" pode ser a soma de `apoiadores[].valor`. Se for calculado, a lista e o total nunca divergem.

## 5. Identidade visual (herdada do Mídia Kit)

- Fundo `#0b0b10` com pontilhado `#1c1c28`, cartões `#14141c`, bordas `#262633`.
- Roxo de destaque `#a24bff` e `#7a2fe0`; dourado `#ffc83d` como acento pontual; texto `#f2f2f7`, texto secundário `#9a9ab0`.
- Título com sombra roxa dura (`3px 3px 0 #3c1470`) e glow.
- Cantos arredondados (20px cartões, 14px botões), botão primário em gradiente roxo.
- Tema escuro por padrão; o Mídia Kit tem tema claro, a replicar na fase 2.
- Cartão do Pix com a cor do midpix.live (roxo).

## 6. Requisitos não funcionais

- Mobile-first (a maior parte do tráfego vem de redes sociais).
- Acessibilidade: contraste mínimo 4.5:1, alvos de toque de 44px, links e botões reais.
- SEO e compartilhamento: title, description, Open Graph e Twitter Card com imagem 1200×630, canonical, hreflang pt/en.
- Performance: imagens em webp com lazy-load, sem frameworks.
- Botão "Copiar chave Pix" com fallback se a Clipboard API falhar.

## 7. Transparência e cuidados

- Mostrar claramente a regra de destino do dinheiro (campeonato) para dar confiança.
- Apoiadores: exibir só apelido, data e valor, e permitir doação anônima. Pedir consentimento para publicar o nome.
- A chave Pix aleatória e o e-mail do PayPal ficam públicos por natureza; conferir antes de publicar que são os corretos.
- Atualizar o arrecadado com frequência e registrar a data da última atualização na página.

## 8. Roadmap

Fase 1, MVP (1 a 2 dias): index.html conforme o mockup, data.json, deploy no GitHub Pages, OG image.
Fase 2: versão em inglês, tema claro, linha do tempo com marcos (ex.: 25%, 50%, 100%), botão de compartilhar.
Fase 3: contador ao vivo do status da live (como no Mídia Kit), galeria dos vlogs após o evento, prestação de contas final (gastos reais).

## 9. Decisões tomadas (24/11/2026)

1. Endereço: forkxx.github.io/mundial.
2. Arrecadado e apoiadores atualizados à mão no `data.json`.
3. Versão em inglês (`en.html`) já no lançamento.
4. Mockup aprovado e site da fase 1 construído no repositório (index.html, en.html, data.json, assets, README).
5. Abertura: tanque circular que enche com o logo do Mundial no centro (conceito 12 de 20). A água sobe conforme `arrecadado` e a soma dos apoiadores no `data.json`.
6. Apoiadores: nuvem neon (conceito 19 de 20). O tamanho do nome é proporcional ao total doado, os 3 maiores em dourado, com a lista completa dentro de "Ver lista completa". Doações do mesmo nome são somadas. Usar apenas apelidos e com consentimento.
7. Sem editor no site: apoiadores e valores são adicionados pedindo ao Claude no projeto, que edita o `data.json`.
8. Regra de arrecadação (25/11/2026): 85% de cada doação conta para a meta e 15% mantém as custas do canal até o evento. No `data.json`, `percentualMeta` vale 85 e cada apoiador guarda o valor bruto doado. A barra e o tanque usam 85% da soma; a nuvem usa o valor bruto. O texto vale para Pix, PayPal e lives (o cartão de lives foi removido).
9. Primeiras 10 doações lançadas (R$ 215,00 brutos, R$ 182,75 para a meta).
10. Ordem das seções (25/11/2026): hero com tanque, nuvem de apoiadores (2ª seção), meta, como ajudar, evento, dúvidas. A nuvem mede cada nome pelo tamanho real (offsetWidth/Height) e testa colisão com folga, então os nomes nunca se sobrepõem. Os ícones de PIX e PayPal são genéricos, não os logotipos oficiais.

11. Melhorias de acabamento (25/11/2026): brasas e brilho no hero; títulos de seção centralizados com ornamento (losango dourado); cartões de "Como ajudar" em moldura de pedra e ouro; galeria de 4 cartões no evento; rodapé completo com redes; barra fixa no celular com mini-progresso e botão Apoiar (aparece depois do hero e some na seção de apoio). Três seções novas ao final, nesta ordem: Divisão da meta (rosca calculada a partir de `custos`), Contagem regressiva ao vivo até `prazo` e Quem é o Forkxx (foto, 41,7 mil seguidores em 5 redes e 1.133 membros no Discord, números tirados do Mídia Kit: atualizar à mão se mudarem).

12. Segunda rodada visual (25/11/2026): chão em perspectiva no hero; título dourado metálico e número em degradê; cartões da meta e do evento em vidro com borda em degradê (os de apoio seguem em pedra e ouro); barra de meta segmentada em 40 blocos; anel rúnico de 60 marcas no tanque (acendem conforme o percentual); menu com barra de rolagem e seção ativa; botões com brilho, variante dourada e foco visível; FAQ em acordeão numerado; entrada em cascata ao rolar; estrelas e anéis pulsando na nuvem; faixas inclinadas de fundo (meta, evento, divisão, quem). Efeitos de movimento respeitam "reduzir animações" e a inclinação 3D só vale com mouse.

## 10. Pendências

- Link direto de pagamento do PayPal (paypal.me), se quiser um botão além do e-mail.
- Trocar a imagem de compartilhamento (`assets/og.png`) por uma arte própria, se desejado.
- Fase 2: tema claro e linha do tempo de marcos.
