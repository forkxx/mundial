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
- Pix (chave aleatória 98547923-1f68-4439-820b-a2eac65629ed) e QR Code via midpix.live
- PayPal: max_lp_rox@hotmail.com
- Doações nas lives: YouTube, Kick e Twitch em /forkxx. 80% de cada doação em live vai para a meta.

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
4. Como ajudar: cartões Pix (QR + chave + botão copiar), PayPal, Lives (80%).
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

## 10. Pendências

- Link direto de pagamento do PayPal (paypal.me), se quiser um botão além do e-mail.
- Trocar a imagem de compartilhamento (`assets/og.png`) por uma arte própria, se desejado.
- Fase 2: tema claro e linha do tempo de marcos.
