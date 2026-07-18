# Tabela Comparativa para o Projeto de Mestrado

Este arquivo foi pensado para uso em duas etapas:

1. **Tabela mestra de leitura**: mais detalhada, para organizar a revisão e registrar decisões.
2. **Quadro sintético para a dissertação**: mais enxuto, para eventual inserção no texto final.

## Orientação de uso

- A **tabela mestra** pode ficar ampla, porque serve como base de trabalho.
- O **quadro sintético** deve ser derivado da tabela mestra, com menos colunas.
- Para dissertação, normalmente um quadro excessivamente largo fica ruim na diagramação. Por isso, o ideal é:
  - manter a tabela completa como material de apoio;
  - e inserir no texto apenas um quadro resumido com os artigos centrais.

## 1. Tabela mestra de leitura e comparação

| Fonte da pesquisa | Ano | Autores | Título | Assunto | Tecnologias usadas | Explicação / justificativa das escolhas | Arquitetura proposta | Pontos positivos | Pontos negativos / limitações | Uso no seu projeto | Status da leitura | DOI / arquivo |
|:--|:--:|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| IEEE | 2024 | Kubascik, M.; Tupy, A.; Sumsky, J.; Baca, T. | *BioLab - Application for Online Analysis Using Lab Streaming Layer for Education and Research Purpose* | LSL, streaming biomédico, arquitetura modular, análise online | Python, MATLAB, LSL, JSON | O artigo não faz comparação formal entre linguagens, mas justifica o uso prático de LSL para streaming/sincronização, Python para aquisição/streaming, MATLAB para análise/visualização e JSON para configuração flexível | Dispositivos biomédicos -> scripts Python -> LSL -> consumidores na rede -> visualização/análise; controlador central com subprocessos e logs | Arquitetura modular; escalabilidade por arquivos JSON; boa inspiração para camada intermediária | Não compara LSL com sockets; não detalha benchmarks de latência; foco maior em ECG/EMG do que em EEG + RV | Base para desenhar a camada intermediária entre CNN e Unity | Lido e resumido | DOI: 10.1109/ICETA63795.2024.10850781 / [biolab.pdf](file:///Users/denisemunchen/Documents/EEG_RV/artigos/LSL/biolab.pdf) |
| IEEE | 2026 | Park, J.-H. et al. | *Toward Practical BCI: A Real-time Wireless Imagined Speech EEG Decoding System* | BCI prático, streaming em tempo real, pipeline ponta a ponta | EEG, LSL, decodificação em tempo real, dispositivo wireless | Justifica LSL pela necessidade de streaming contínuo e operação em tempo real entre aquisição e decodificador personalizado | Pipeline ponta a ponta para captura, streaming e classificação online | Forte para justificar arquitetura operacional real | Não é focado em RV nem em mão virtual | Referência para pipeline entre classificador e aplicação final | Leitura parcial por abstract/metadados | DOI: 10.1109/BCI69045.2026.11435050 |
| IEEE | 2026 | Roque, T. R. et al. | *Real-Time Mobile EEG Hyperscanning: A Precise and Accessible Platform for Social Brain-Computer Interfaces* | Sincronização, jitter, drift, latência, EEG móvel | LSL, OpenBCI, sincronização por hardware e software | Mostra que LSL sozinho pode introduzir limitações de sincronização; justifica arquitetura híbrida quando precisão temporal é crítica | Plataforma móvel com sincronização por trigger wireless + software customizado | Excelente para discutir limites reais de sincronização | Foco em hyperscanning social, não em RV terapêutica | Fundamentação técnica para seção de sincronização e latência | Leitura parcial por abstract/metadados | DOI: 10.1109/JSEN.2025.3597568 |
| IEEE | 2018 | Claucich, C.; Carrere, L. C.; Tabernig, C. B. | *Virtual Reality Interface Built Using Unity3D for Rehabilitation with BCI Systems Based on Motor Imagery* | BCI, Unity3D, RV, reabilitação motora | Unity3D, BCI por imagética motora | Justifica escolhas por necessidade de comunicação rápida em tempo real, interface motivadora e adequação a hardware de gama média | Sistema BCI -> módulo de realimentação visual em Unity3D -> avatar/movimento terapêutico | Muito próximo do seu caso de uso | Abstract não detalha protocolo de comunicação | Referência aplicada central para EEG + mão virtual + Unity | Leitura parcial por abstract | IEEE ARGENCON 2018 |
| IEEE | 2022 | Li, P. et al. | *Virtual Reality Roaming System Design Based on Motor Imagery-Based Brain-Computer Interface* | Comunicação em tempo real entre BCI e cena virtual | Unity, imagética motora, LBP, SVM | Justifica o mecanismo de comunicação em tempo real para controlar o humano virtual na cena | Plataforma BCI -> mecanismo de comunicação em tempo real -> cena Unity | Alinha bem com o problema de levar o comando à engine | Não deixa claro se usa LSL, socket ou outro middleware | Apoio para arquitetura aplicada e integração BCI-RV | Leitura parcial por abstract | IEEE ITOEC 2022 |
| IEEE | 2016 | Wang, Z.; Healy, G.; Smeaton, A. F.; Ward, T. E. | *An investigation of triggering approaches for the rapid serial visual presentation paradigm in brain computer interfacing* | Timing, triggers, precisão temporal | BCI, software triggers, hardware triggers, LSL | Justifica a necessidade de validar o tempo físico real, e não apenas confiar no evento de software | Comparação entre marcação por software e trigger físico | Muito forte para a discussão metodológica de sincronização | Não trata de RV nem de Unity | Base para justificar cautela com tempo de evento e sincronização | Leitura parcial por abstract/metadados | DOI: 10.1109/ISSC.2016.7528466 |
| IEEE | 2025 | Nemes, Á. G. et al. | *Temporal Coupling of Brain Signals and Fine Motor Output Using Affordable EEG* | Integração temporal, motricidade fina, ambiente virtual | EEG acessível, LSL, deep learning, ambiente virtual | Justifica LSL para alinhamento multimodal em nível de milissegundos | EEG + eventos + saída motora sincronizados em pipeline temporal | Muito aderente ao seu foco de movimento e ambiente virtual | Não é um artigo centrado em engine de RV | Apoio forte para relacionamento entre EEG e ação motora virtual | Leitura parcial por abstract/metadados | DOI: 10.1109/ACCESS.2025.3587262 |
| IEEE | 2024 | Lin, K. et al. | *Motor Imagery Performance through Embodied Digital Twins in a Virtual Reality-Enabled BCI Environment* | Digital twin, BCI, RV, representação corporal | RV, BCI, embodied digital twin | Ajuda a justificar a mão virtual como representação incorporada do usuário | Ambiente BCI habilitado para RV com avatar/gêmeo digital | Muito útil para pensar a modelagem da mão virtual | Menos focado em middleware/latência | Referência para a camada de representação na Unity | Leitura parcial por abstract/metadados | DOI: 10.3791/66859 |
| Artigo-semente | 2013 | Kothe, C. A.; Makeig, S. | *BCILAB: a platform for brain-computer interface development* | Plataforma BCI, software, ecossistema | BCILAB, plataforma BCI | Artigo-semente para base conceitual de plataforma de desenvolvimento | Plataforma para desenvolvimento BCI | Pode fortalecer a fundamentação técnica | Ainda não incorporado à leitura | Base conceitual, se necessário | Pendente | Buscar PDF |
| Artigo-semente | 2018 | Kerous, B.; Skola, F.; Liarokapis, F. | *EEG-based BCI and video games: a progress report* | BCI, jogos, engines, aplicações interativas | EEG, BCI, jogos, possivelmente Unity/RV | Bom elo entre BCI e aplicações interativas em engine | Revisão/progresso de aplicações em jogos | Útil para transição entre BCI e Unity | Ainda não lido | Apoio para seção de aplicações interativas | Pendente | Buscar PDF |

## 2. Quadro sintético para inserção na dissertação

Este modelo é mais adequado para o texto final do trabalho.

| Autores/Ano | Título | Assunto principal | Tecnologias / arquitetura | Contribuição para este projeto | Limitação principal |
|:--|:--|:--|:--|:--|:--|
| Kubascik et al. (2024) | *BioLab - Application for Online Analysis Using Lab Streaming Layer for Education and Research Purpose* | Streaming biomédico e arquitetura modular | Python, MATLAB, LSL, JSON | Inspira a camada intermediária entre classificador e aplicação final | Não compara LSL com outras soluções |
| Park et al. (2026) | *Toward Practical BCI: A Real-time Wireless Imagined Speech EEG Decoding System* | Pipeline BCI em tempo real | EEG, LSL, streaming contínuo | Sustenta a ideia de pipeline operacional ponta a ponta | Não é focado em RV |
| Roque et al. (2026) | *Real-Time Mobile EEG Hyperscanning...* | Sincronização e latência | LSL + sincronização híbrida | Justifica cuidado com jitter, drift e precisão temporal | Foco diferente do caso terapêutico |
| Claucich et al. (2018) | *Virtual Reality Interface Built Using Unity3D for Rehabilitation with BCI Systems Based on Motor Imagery* | Integração BCI + Unity para reabilitação | Unity3D + BCI por imagética motora | Muito próximo do caso de uso da mão virtual | Pouco detalhe sobre middleware |
| Li et al. (2022) | *Virtual Reality Roaming System Design Based on Motor Imagery-Based Brain-Computer Interface* | Comunicação entre BCI e cena virtual | Unity + classificador MI | Apoia a ponte entre inferência e cena virtual | Protocolo de comunicação não detalhado |
| Wang et al. (2016) | *An investigation of triggering approaches...* | Precisão temporal | Trigger por software vs. hardware | Reforça a validação do tempo dos eventos | Não trata de RV |

## 3. Colunas extras que você pode preencher depois

Se quiser enriquecer a tabela mestra mais adiante, estas colunas costumam ajudar bastante:

- `Tipo de estudo`
- `Base de dados`
- `População / participantes`
- `Sinal usado`
- `Saída do sistema`
- `Métrica principal`
- `Latência reportada`
- `Compara com outra tecnologia?`
- `Arquivo PDF salvo?`
- `Trechos úteis para citação`

## 4. Recomendação para a dissertação

Minha sugestão é usar:

- este arquivo como **planilha de análise conceitual e técnica**;
- a [tabela_padrao_ouro_artigo.md](file:///Users/denisemunchen/Documents/EEG_RV/documentos/referencias/tabela_padrao_ouro_artigo.md) como **visão estratégica da revisão**;
- e, no texto final da dissertação, inserir apenas o **quadro sintético** com os 4 a 8 artigos mais centrais.
