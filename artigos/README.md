# Fluxo de Artigos

Esta estrutura foi criada para organizar artigos localizados nas bases e gerar um resumo inicial de cada arquivo extraido.

## Pastas

- `00_buscas`: estrategias de busca, consultas booleanas e exports das bases.
- `01_extraidos`: textos extraidos dos artigos em formatos como `.txt`, `.md` e `.html`.
- `02_resumos`: resumos gerados automaticamente, um arquivo por artigo.
- `03_planilhas`: arquivos consolidados, como indice CSV dos resumos.

## Como usar

1. Coloque os arquivos de texto extraido em `artigos/01_extraidos`.
2. Rode o script:

```bash
python3 artigos/gerar_resumos.py
```

3. Consulte os resumos em `artigos/02_resumos`.
4. Consulte o indice consolidado em `artigos/03_planilhas/resumos_index.csv`.

## Observacoes

- O script nao depende de APIs externas.
- O resumo gerado e inicial e heuristico; ele serve para triagem rapida.
- Se depois voce quiser, posso evoluir esse fluxo para gerar fichamento, extracao de metadados e tabela de elegibilidade.
