# Forkão no Raraland!!

Site para divulgar e arrecadar fundos para o Forkxx ir ao Mundial de Warcraft 3 (Being Esports World Series 2027, Scholl Hundisburg, Alemanha, 11 a 14/03/2027).

Publicado em: https://forkxx.github.io/mundial/

## Como atualizar

Tudo que muda fica em `data.json`:

- `percentualMeta`: parte de cada doação que conta para a meta (hoje 85). Os 15% restantes mantêm as custas do canal. Se mudar, o texto do site acompanha o número.
- `atualizado`: data da última atualização (AAAA-MM-DD).
- `apoiadores`: lista com o valor bruto doado, no formato `{ "nome": "Apelido", "data": "AAAA-MM-DD", "valor": 50 }`. Use só apelido.
- `meta`, `prazo`, `custos`: só mudam se o plano mudar.

Depois edite no GitHub (ícone de lápis), faça commit e o site atualiza em alguns minutos. No dia a dia, a atualização é pedida ao Claude no projeto "Site Rumo ao Mundial", que edita o `data.json`.

## Estrutura

- `index.html`: versão em português. `en.html`: versão em inglês. Os textos de ambas são iguais em estrutura, então qualquer mudança de layout deve ser feita nas duas.
- `data.json`: dados dinâmicos.
- `assets/`: favicon, foto, QR do Pix e imagem de compartilhamento (`og.png`, 1200×630).

Site estático em HTML, CSS e JS puros, sem build. Para testar localmente: `python3 -m http.server` na pasta e abrir `localhost:8000`.
