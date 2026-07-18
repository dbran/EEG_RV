# Método Implementado

## Objetivo

O método implementado teve como objetivo viabilizar a integração entre a saída de um classificador baseado em EEG e uma aplicação de Realidade Virtual desenvolvida na Unity, de modo que comandos motores inferidos a partir da atividade cerebral pudessem ser convertidos em resposta visual por meio de uma mão virtual tridimensional.

Nesta etapa do projeto, o foco não foi a classificação do EEG em si, mas a construção e validação da camada de comunicação entre:

1. a saída do classificador;
2. um módulo intermediário de tradução de dados;
3. a aplicação de Realidade Virtual;
4. o objeto visual responsável pelo feedback ao usuário.

## Visão Geral da Arquitetura

O protótipo implementado foi organizado em uma arquitetura modular composta por cinco blocos principais:

```text
EEG -> CNN/classificador -> JSONL -> tradutor Python -> UDP -> Unity -> mão 3D
```

Em termos funcionais, essa arquitetura separa:

- a etapa de aquisição e classificação do sinal;
- a etapa de tradução semântica da saída do classificador;
- a etapa de transporte do comando;
- a etapa de renderização e resposta visual em ambiente virtual.

Essa separação foi adotada para evitar que a engine de RV precisasse manipular diretamente o EEG bruto ou a lógica interna do classificador, recebendo apenas comandos motores simplificados.

## Fonte de Dados

A entrada utilizada nesta etapa foi um arquivo no formato `JSONL`, contendo um objeto JSON por linha, representando eventos produzidos pela etapa de classificação. Esse formato permitiu simular e testar o comportamento do sistema sem depender, a cada execução, da aquisição online do EEG.

Foram considerados, principalmente, dois tipos de evento:

1. `started`, usado para informar o início da sessão;
2. `inference`, usado para representar o resultado da inferência do classificador.

O evento `started` não gera movimento na Unity. Apenas os eventos `inference` são elegíveis para conversão em comando motor.

## Tradução dos Dados no Python

Foi desenvolvido um script em Python para atuar como módulo intermediário entre a saída do classificador e a Unity. Esse módulo foi responsável por:

1. ler o arquivo `JSONL`;
2. filtrar eventos inválidos;
3. interpretar os campos relevantes da inferência;
4. traduzir a saída do classificador para um conjunto reduzido de comandos;
5. emitir os comandos em formato JSON simplificado;
6. enviar esses comandos à Unity por UDP.

Os principais campos considerados na inferência foram:

- `type`
- `label`
- `label_text`
- `rejected`
- `is_mi`
- `p_move`
- `tau`
- `group_id`

Nesta implementação, `is_mi` foi interpretado como indicador da presença de imagética motora, enquanto `tau` foi interpretado como limiar de decisão associado ao valor `p_move`.

## Regras de Aceitação

Para reduzir ruído durante a integração inicial, foram adotadas regras simples de aceitação do evento. Um evento só é convertido em comando quando:

1. `type == "inference"`;
2. `rejected == false`;
3. `label_text` está presente.

Além disso, para comandos motores ativos, a implementação considera:

1. `is_mi == true`;
2. `p_move > tau`.

Caso essas condições não sejam satisfeitas, o sistema mantém o estado neutro.

## Mapeamento de Classes para Comandos

A saída textual do classificador foi mapeada para três comandos discretos:

| Classe original | Comando gerado |
|:--|:--|
| `SEM MOVIMENTO` | `no_move` |
| `ESQUERDA` | `left` |
| `DIREITA` | `right` |

Esse mapeamento foi adotado para desacoplar o modelo de classificação da lógica de controle da Unity, permitindo que a engine trabalhasse apenas com comandos de alto nível.

## Formato da Mensagem

Após a tradução, o Python passou a emitir mensagens JSON simplificadas, contendo pelo menos:

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

Esse formato preserva informações suficientes para rastreabilidade e depuração, sem sobrecarregar a Unity com dados desnecessários para o controle visual.

## Comunicação com a Unity

Como mecanismo de transporte, foi adotado o protocolo UDP em rede local. A escolha do UDP, nesta fase do projeto, deveu-se principalmente à sua simplicidade de implementação e ao baixo acoplamento entre os módulos.

Na prática, o módulo Python envia os comandos para uma porta local, enquanto a Unity permanece escutando essa porta por meio de um receptor dedicado.

Para facilitar a validação visual, a implementação passou a aceitar um atraso opcional entre os comandos emitidos, evitando que múltiplos eventos fossem processados rápido demais a ponto de mascarar a observação do comportamento do objeto virtual.

## Implementação na Unity

Na Unity, a solução foi organizada em dois componentes principais:

1. `BCIDebugController`
2. `BCIUDPReceiver`

O componente `BCIDebugController` ficou responsável por:

- manter a referência ao objeto visual controlado;
- aplicar os comandos `left`, `right` e `no_move`;
- atualizar os textos de estado na interface;
- executar o comportamento local de teste por teclado.

O componente `BCIUDPReceiver` ficou responsável por:

- escutar a porta UDP configurada;
- receber as mensagens enviadas pelo Python;
- desserializar o JSON recebido;
- enfileirar os comandos recebidos;
- encaminhar os comandos ao `BCIDebugController`.

O uso de uma fila de comandos foi necessário para evitar perda perceptível de eventos quando vários pacotes chegavam em sequência muito rápida.

## Configuração da Cena

A cena inicial de teste foi composta pelos seguintes elementos:

- câmera principal;
- iluminação básica;
- plano de referência;
- `Canvas` com textos de estado;
- objeto controlador;
- objeto visual representando a mão.

Em uma primeira fase, utilizou-se um cubo (`HandProxy`) como proxy visual. Essa decisão permitiu validar:

1. a lógica de aplicação dos comandos;
2. a atualização da interface;
3. a comunicação entre Python e Unity.

Após a validação do fluxo básico, o cubo foi substituído por um modelo tridimensional de mão (`Rigged Hand`), mantido sob a mesma lógica de controle. Com isso, o protótipo passou a operar com uma representação visual mais próxima do cenário final do projeto.

## Uso de `runInBackground`

Durante os testes no Editor da Unity, foi observado que a aplicação deixava de responder visualmente quando perdia foco para o terminal utilizado na execução do script Python. Para corrigir esse comportamento, foi adicionada a instrução:

```csharp
Application.runInBackground = true;
```

nos componentes Unity responsáveis pela recepção e aplicação dos comandos. Essa modificação permitiu que o loop da aplicação continuasse processando os eventos mesmo quando a janela do Editor não estava em primeiro plano.

## Estratégia de Validação

A validação do método implementado foi realizada de forma incremental, em três etapas:

1. validação local na Unity com entrada por teclado;
2. validação da comunicação via UDP entre Python e Unity;
3. validação da substituição do cubo por uma mão 3D.

Os comandos testados foram:

- `left`
- `right`
- `no_move`

O critério de sucesso, nesta fase, foi verificar se:

1. o comando era corretamente produzido pelo módulo Python;
2. a Unity o recebia sem erro;
3. o objeto visual respondia de forma coerente;
4. a interface exibia o estado correspondente.

## Resultado da Etapa Implementada

Ao final desta etapa, o protótipo passou a apresentar funcionamento ponta a ponta, com o seguinte encadeamento:

```text
EEG/CNN -> JSONL -> Python -> UDP -> Unity -> mão 3D
```

Esse resultado demonstra a viabilidade da camada de comunicação entre a saída do classificador e a aplicação de Realidade Virtual, constituindo uma base funcional para as próximas etapas do projeto.

## Limitações Atuais

Apesar da validação do fluxo de integração, a implementação atual ainda apresenta limitações importantes:

1. os comandos aplicam deslocamentos simples, e não animações motoras completas;
2. a mão virtual ainda não está integrada a uma cena terapêutica final;
3. a entrada utilizada nesta etapa foi baseada em arquivo `JSONL`, e não em streaming online contínuo do classificador;
4. ainda não foi realizada avaliação sistemática de latência ponta a ponta.

## Próximos Passos

Os próximos passos previstos a partir deste método implementado são:

1. consolidar a hierarquia final da mão 3D na Unity;
2. substituir deslocamentos simples por animações ou gestos;
3. integrar a mão virtual a uma cena de reabilitação;
4. avaliar temporalmente o comportamento da comunicação entre emissão do comando e resposta visual;
5. evoluir do teste baseado em `JSONL` para integração com saída online do classificador.
