# Decisoes Tecnicas do Prototipo

## Objetivo

Este documento registra as principais decisoes tecnicas adotadas na implementacao inicial do prototipo de integracao entre a saida do classificador de EEG e a representacao de uma mao virtual em ambiente Unity. O objetivo e explicitar as justificativas de projeto, facilitar a rastreabilidade das escolhas e oferecer base textual para reutilizacao na redacao da dissertacao.

## Por que Python

Python foi adotado como linguagem da camada intermediaria de traducao entre a saida do classificador e a engine de realidade virtual por quatro motivos principais.

Primeiro, Python ja estava naturalmente inserido no fluxo de processamento do projeto, especialmente no contexto de leitura dos arquivos `JSONL`, manipulacao dos resultados da CNN e prototipacao rapida de regras de decisao. Isso reduziu a necessidade de introduzir uma nova linguagem na etapa de processamento dos comandos.

Segundo, Python oferece alta velocidade de desenvolvimento para tarefas de integracao. A implementacao de leitura de inferencias, validacao dos campos `label_text`, `is_mi`, `p_move` e `tau`, e conversao para comandos simplificados foi realizada com baixa complexidade e alta legibilidade.

Terceiro, Python possui bibliotecas e recursos maduros para manipulacao de arquivos, rede e automacao local, o que favorece iteracoes frequentes no prototipo. Isso e particularmente relevante na fase inicial do trabalho, em que o foco esta mais na validacao da arquitetura do que na otimizacao final de desempenho.

Quarto, o uso de Python preserva uma separacao clara entre as responsabilidades do sistema: o lado de classificacao e traducao permanece fora da engine grafica, enquanto a Unity fica concentrada na recepcao de comandos e na resposta visual.

## Por que UDP nesta fase

O protocolo UDP foi escolhido nesta etapa do prototipo como mecanismo de comunicacao entre o tradutor Python e a Unity por sua simplicidade de implementacao e baixo acoplamento.

Do ponto de vista pratico, o UDP permitiu validar rapidamente a transmissao de comandos `left`, `right` e `no_move` sem a necessidade de estabelecer conexoes persistentes, gerenciar estados complexos de sessao ou introduzir dependencias adicionais na Unity. Isso acelerou a prova de conceito da ponte entre processamento e visualizacao.

Outra justificativa importante e que, nesta fase, o sistema transmite comandos discretos e de pequeno volume, e nao fluxos densos de sinal bruto. Nesse contexto, a leveza do UDP e suficiente para a validacao funcional do pipeline.

Adicionalmente, o uso de UDP facilita testes locais, repetiveis e de baixa friccao entre processos distintos em uma mesma maquina. Assim, o protocolo se mostrou adequado como escolha de prototipacao arquitetural.

Essa decisao nao implica que o UDP seja necessariamente a solucao final do sistema. Em fases futuras, a arquitetura pode evoluir para mecanismos com maior controle de entrega, sincronizacao ou integracao com outras camadas do sistema, conforme as demandas experimentais e os requisitos de robustez aumentem.

## Por que Unity

A Unity foi escolhida como engine de realidade virtual e visualizacao por combinar maturidade tecnica, ampla documentacao e forte adequacao a prototipos interativos em tempo real.

No contexto deste projeto, a Unity oferece vantagens diretas: suporte consolidado a objetos 3D, facilidade de importacao de assets como maos rigadas, integracao com scripts em C#, ambiente visual de edicao e ampla disponibilidade de materiais, exemplos e suporte da comunidade. Essas caracteristicas reduziram a barreira de entrada para a construcao da cena experimental e da mao virtual.

Outro fator relevante e que a Unity permite separar com clareza a logica de recepcao dos comandos e a camada de representacao visual. Isso favorece a modularidade do sistema e a futura evolucao do prototipo para animacoes, gestos, interacoes mais sofisticadas e eventual integracao com dispositivos de realidade virtual.

Do ponto de vista metodologico, a Unity tambem e apropriada porque permite construir rapidamente cenas controladas para validacao experimental, com feedback visual observavel e repetivel. Isso e importante para o desenvolvimento incremental do sistema e para a apresentacao dos resultados.

## Por que usar um comando intermediario em vez de enviar EEG bruto para a engine

A decisao de utilizar um comando intermediario, como `left`, `right` ou `no_move`, em vez de transmitir o EEG bruto diretamente para a Unity, foi central para a clareza arquitetural do prototipo.

O primeiro motivo e a separacao de responsabilidades. O EEG bruto pertence a camada de aquisicao e processamento de sinais, enquanto a Unity foi adotada como camada de representacao e feedback. Ao enviar apenas o resultado semantico da inferencia, evita-se transferir para a engine grafica tarefas que nao pertencem ao seu nucleo funcional.

O segundo motivo e a reducao de complexidade. Enviar EEG bruto para a Unity exigiria que a engine passasse a lidar com sinais multicanais, frequencias de amostragem, filtros, janelas temporais e regras de classificacao, o que aumentaria drasticamente o acoplamento entre processamento de sinais e visualizacao.

O terceiro motivo e a robustez do prototipo. Um comando intermediario e mais simples de testar, depurar, registrar e repetir experimentalmente. Isso permite verificar se a ponte entre os modulos esta correta antes de evoluir para comportamentos visuais mais complexos.

O quarto motivo e a extensibilidade. Mantendo uma interface de comunicacao baseada em comandos abstratos, torna-se mais facil substituir o classificador, alterar os criterios de traducao ou trocar a representacao visual sem reescrever toda a arquitetura.

Em sintese, o uso de comandos intermediarios funciona como uma interface de desacoplamento entre o dominio neurofisiologico e o dominio grafico-interativo. Essa estrategia torna o sistema mais modular, compreensivel e evolutivo.

## Sintese

As decisoes adotadas nesta etapa podem ser resumidas da seguinte forma:

- `Python` foi escolhido como camada intermediaria por sua rapidez de desenvolvimento, integracao natural com o fluxo de classificacao e facilidade de manipulacao de arquivos e rede.
- `UDP` foi adotado como mecanismo de comunicacao por sua simplicidade e adequacao a um prototipo funcional baseado em comandos discretos.
- `Unity` foi escolhida como engine por sua maturidade para visualizacao 3D, facilidade de prototipacao e potencial de expansao para RV.
- `Comandos intermediarios` foram utilizados para desacoplar o processamento de EEG da representacao visual, reduzindo a complexidade do sistema.

## Relacao com a arquitetura implementada

As decisoes descritas neste documento se refletem diretamente no pipeline validado ate o momento:

```text
EEG/CNN -> JSONL -> tradutor Python -> UDP -> Unity -> mao virtual 3D
```

Esse arranjo permitiu construir uma prova de conceito funcional, modular e suficientemente clara para sustentar as proximas etapas de refinamento do sistema.
