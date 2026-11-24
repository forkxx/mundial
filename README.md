# Forkão no Raraland!!

Site para divulgar e arrecadar fundos para o Forkxx ir ao Mundial de Warcraft 3 (Being Esports World Series 2027, Scholl Hundisburg, Alemanha, 11 a 14/03/2027).

Publicado em: https://forkxx.github.io/mundial/

## Como atualizar

Tudo que muda fica em `data.json`:

- `arrecadado`: total arrecadado em reais. O site usa o maior valor entre este campo e a soma dos apoiadores.
- `atualizado`: data da última atualização (AAAA-MM-DD).
- `apoiadores`: lista de `{ "nome": "Apelido", "data": "AAAA-MM-DD", "valor": 50 }`. Use só apelido.
- `meta`, `prazo`, `custos`: só mudam se o plano mudar.

Depois edite no GitHub (ícone de lápis), faça commit e o site atualiza em alguns minutos.

## Estrutura

- `index.html`: versão em português. `en.html`: versão em inglês. Os textos de ambas são iguais em estrutura, então qualquer mudança de layout deve ser feita nas duas.
- `data.json`: dados dinâmicos.
- `assets/`: favicon, foto, QR do Pix e imagem de compartilhamento (`og.png`, 1200×630).

Site estático em HTML, CSS e JS puros, sem build. Para testar localmente: `python3 -m http.server` na pasta e abrir `localhost:8000`.
