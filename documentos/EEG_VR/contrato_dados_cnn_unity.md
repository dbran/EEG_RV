# Contrato de Dados: CNN -> Unity

## Objetivo

Definir a primeira versao do contrato de dados entre a saida do classificador EEG/CNN e a aplicacao de Realidade Virtual na Unity.

Este contrato usa como referencia o arquivo:

- [bci_stream_example.jsonl](file:///Users/denisemunchen/Documents/EEG_RV/python/bci_stream_example.jsonl)

## Escopo

Este documento cobre:

- o formato de entrada gerado pela etapa de inferencia;
- as regras minimas para aceitar ou ignorar um evento;
- o formato de comando simplificado que sera enviado para a Unity.

Este documento nao cobre ainda:

- protocolo de transporte final (`socket`, `LSL` ou outro);
- animacao detalhada da mao;
- sincronizacao fina entre evento neural e renderizacao.

## Fonte de entrada

A entrada atual e um arquivo `JSONL`, com um objeto JSON por linha.

Existem pelo menos dois tipos de evento:

1. `started`
2. `inference`

### Evento `started`

Usado para informar que a sessao foi iniciada.

Exemplo:

```json
{"type":"started","sim":true,"mode":"screen","modality":"mi","threshold":0.45,"group_id":0,"sfreq":160.0,"n_channels":8,"hand_connected":null}
```

Esse evento **nao deve gerar movimento na Unity**.

### Evento `inference`

Usado para informar o resultado atual da inferencia da CNN/classificador.

Exemplo:

```json
{"type":"inference","label":1,"label_text":"ESQUERDA","rejected":false,"is_mi":true,"p_move":0.831,"tau":0.45,"group_id":0,"hand":null}
```

## Campos de interesse na entrada

Para a primeira integracao com a Unity, os campos mais importantes sao:

| Campo | Tipo | Papel no contrato |
|:--|:--|:--|
| `type` | string | Distingue evento de inicio e evento de inferencia |
| `label` | inteiro | Classe numerica prevista |
| `label_text` | string | Classe em texto, usada como base do comando |
| `rejected` | boolean | Indica se a inferencia deve ser ignorada |
| `is_mi` | boolean | Indica se houve deteccao de imagetica motora |
| `p_move` | numero | Confianca/indicador de movimento |
| `tau` | numero | Limiar usado para decisao |
| `group_id` | inteiro | Identificador de agrupamento/sessao |

### Definicao operacional de `is_mi`

`is_mi` deve ser interpretado, nesta primeira versao, como:

- `true`: o sistema considera que ha imagetica motora ativa ou movimento imaginado detectavel;
- `false`: o sistema considera que nao ha imagetica motora suficiente para tratar o evento como comando motor.

No projeto, esse campo funciona como um indicador booleano de validade motora.

### Definicao operacional de `tau`

`tau` deve ser interpretado como o limiar de decisao adotado pelo classificador para validar a presenca de movimento.

Leitura operacional:

- `p_move > tau`: ha evidencia suficiente para considerar movimento;
- `p_move <= tau`: nao ha evidencia suficiente para considerar movimento.

Na pratica, `tau` funciona como um valor de corte, enquanto `p_move` representa a intensidade ou confianca associada ao evento.

## Regras de aceitacao do evento

Um evento so pode ser convertido em comando para a Unity quando atender a todas as regras abaixo:

1. `type == "inference"`
2. `rejected == false`
3. `label_text` presente

### Regra recomendada para a primeira versao

Para reduzir ruido na integracao inicial, recomenda-se aceitar comando apenas quando:

1. `type == "inference"`
2. `rejected == false`
3. `is_mi == true`

Observacao:

- `p_move` e `tau` devem ser registrados e preservados, mas nesta primeira versao podem funcionar como campos de apoio, nao como bloqueio principal.

## Mapeamento de classes para comando

| `label` | `label_text` | Comando Unity |
|:--:|:--|:--|
| 0 | `SEM MOVIMENTO` | `no_move` |
| 1 | `ESQUERDA` | `left` |
| 2 | `DIREITA` | `right` |

Se surgir qualquer outro valor, a saida deve cair para:

```json
{"command":"no_move"}
```

## Formato de saida para a Unity

A Unity nao precisa receber o EEG bruto. Ela deve receber apenas um comando motor simplificado.

Formato minimo sugerido:

```json
{
  "command": "left",
  "source_label": 1,
  "source_label_text": "ESQUERDA",
  "is_mi": true,
  "p_move": 0.831,
  "tau": 0.45,
  "group_id": 0
}
```

## Regras de traducao

### Caso 1: movimento para esquerda

Entrada:

```json
{"type":"inference","label":1,"label_text":"ESQUERDA","rejected":false,"is_mi":true,"p_move":0.831,"tau":0.45,"group_id":0}
```

Saida:

```json
{"command":"left","source_label":1,"source_label_text":"ESQUERDA","is_mi":true,"p_move":0.831,"tau":0.45,"group_id":0}
```

### Caso 2: movimento para direita

Entrada:

```json
{"type":"inference","label":2,"label_text":"DIREITA","rejected":false,"is_mi":true,"p_move":0.901,"tau":0.45,"group_id":0}
```

Saida:

```json
{"command":"right","source_label":2,"source_label_text":"DIREITA","is_mi":true,"p_move":0.901,"tau":0.45,"group_id":0}
```

### Caso 3: sem movimento

Entrada:

```json
{"type":"inference","label":0,"label_text":"SEM MOVIMENTO","rejected":false,"is_mi":false,"p_move":0.17,"tau":0.45,"group_id":0}
```

Saida:

```json
{"command":"no_move","source_label":0,"source_label_text":"SEM MOVIMENTO","is_mi":false,"p_move":0.17,"tau":0.45,"group_id":0}
```

## Comportamento esperado na Unity

| Comando | Acao esperada |
|:--|:--|
| `left` | mover/animar a mao para a esquerda |
| `right` | mover/animar a mao para a direita |
| `no_move` | manter a mao em repouso ou estado neutro |

## Primeira arquitetura recomendada

```text
EEG -> CNN/classificador -> JSONL -> tradutor Python -> comando simplificado -> Unity
```

## Proximos passos

1. implementar um script Python tradutor de `jsonl` para comando simplificado;
2. testar a traducao com o arquivo de exemplo;
3. enviar o comando para a Unity por um canal simples, preferencialmente `socket`;
4. validar primeiro com um objeto simples antes da mao 3D.

## Observacoes

- Este e um contrato inicial e pode ser revisado quando os testes com a Unity comecarem.
- Se surgirem novas classes da CNN, a tabela de mapeamento deve ser atualizada neste arquivo antes da integracao.
- A validacao atual ja foi feita com uma mao 3D na Unity, mantendo o mesmo contrato de comandos `left`, `right` e `no_move`.
