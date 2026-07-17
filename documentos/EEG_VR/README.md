# EEG_VR - Documentacao Consolidada

## Objetivo

Reunir em um unico ponto os documentos e arquivos principais da etapa atual do prototipo `EEG -> CNN -> Unity`.

## Estado atual

O que ja foi feito:

1. definicao do contrato inicial de dados entre a saida da CNN e a Unity;
2. criacao da cena de teste no Unity com `Canvas`, `TextMeshPro` e `HandProxy`;
3. validacao da logica local por teclado com `left`, `right` e `no_move`;
4. preparacao da ponte Python -> UDP -> Unity;
5. validacao da recepcao UDP na Unity;
6. identificacao e correcao da necessidade de `Application.runInBackground = true` nos dois scripts Unity;
7. substituicao do cubo por uma mao 3D (`Rigged Hand`) na cena;
8. validacao da resposta da mao 3D aos comandos `left`, `right` e `no_move`;
9. organizacao dos arquivos de apoio para a escrita do metodo.

## Ordem recomendada de leitura

1. [contrato_dados_cnn_unity.md](file:///Users/denisemunchen/Documents/EEG_RV/documentos/EEG_VR/contrato_dados_cnn_unity.md)
2. [Unity_step_by_step.md](file:///Users/denisemunchen/Documents/EEG_RV/documentos/EEG_VR/Unity_step_by_step.md)
3. [BCIUDPReceiver.cs](file:///Users/denisemunchen/Documents/EEG_RV/documentos/EEG_VR/BCIUDPReceiver.cs)
4. [bci_jsonl_to_unity_commands.py](file:///Users/denisemunchen/Documents/EEG_RV/python/bci_jsonl_to_unity_commands.py)

## Arquivos-chave

### Contrato de dados

- [contrato_dados_cnn_unity.md](file:///Users/denisemunchen/Documents/EEG_RV/documentos/EEG_VR/contrato_dados_cnn_unity.md)

Define:

- campos de interesse do `jsonl`;
- significado operacional de `is_mi` e `tau`;
- regras de aceitacao;
- mapeamento `SEM MOVIMENTO -> no_move`, `ESQUERDA -> left`, `DIREITA -> right`.

### Guia da Unity

- [Unity_step_by_step.md](file:///Users/denisemunchen/Documents/EEG_RV/documentos/EEG_VR/Unity_step_by_step.md)

Documenta:

- criacao do projeto;
- configuracao da cena;
- `Canvas` e textos;
- `BCIDebugController`;
- uso do `Input System`;
- preparo do teste UDP;
- problemas encontrados e solucoes.

### Receptor UDP da Unity

- [BCIUDPReceiver.cs](file:///Users/denisemunchen/Documents/EEG_RV/documentos/EEG_VR/BCIUDPReceiver.cs)

Responsavel por:

- ouvir pacotes UDP na porta configurada;
- ler o JSON recebido;
- repassar o comando para o `BCIDebugController`;
- enfileirar os comandos para evitar perda visual quando os pacotes chegam muito rapido.

### Tradutor Python

- [bci_jsonl_to_unity_commands.py](file:///Users/denisemunchen/Documents/EEG_RV/python/bci_jsonl_to_unity_commands.py)
- [rodar_bci_bridge.sh](file:///Users/denisemunchen/Documents/EEG_RV/python/rodar_bci_bridge.sh)
- [bci_stream_example.jsonl](file:///Users/denisemunchen/Documents/EEG_RV/python/bci_stream_example.jsonl)

Responsavel por:

- ler o `jsonl` gerado pela CNN;
- filtrar eventos validos;
- emitir `no_move`, `left` e `right`;
- enviar os comandos para a Unity por UDP;
- usar por padrao um arquivo `bci_stream_example.jsonl` relativo ao proprio script, sem caminho absoluto da maquina local.

## Arquitetura atual

```text
EEG -> CNN/classificador -> JSONL -> tradutor Python -> UDP -> Unity -> BCIDebugController -> HandRoot/Rigged Hand
```

## Proximo passo

1. consolidar a hierarquia final da mao 3D na cena;
2. trocar o deslocamento simples por animacao/gesto;
3. definir o comportamento visual de `left`, `right` e `no_move`;
4. integrar a cena de teste com a cena de reabilitacao.

## Observacao de implementacao

Durante os testes no Editor da Unity, foi observado que o cubo so respondia apos o retorno do foco para a interface. A correcao foi adicionar:

```csharp
Application.runInBackground = true;
```

no `Start()` de `BCIDebugController` e `BCIUDPReceiver`.

## Marco atual

O prototipo ja foi validado ponta a ponta:

```text
EEG/CNN -> JSONL -> Python -> UDP -> Unity -> mao 3D
```

Isso significa que:

- a traducao de inferencias para comandos funciona;
- a comunicacao UDP funciona;
- a Unity recebe e aplica os comandos;
- a mao 3D ja responde aos comandos no lugar do cubo de teste.
