# Tabela Padrão Ouro para o Artigo

Esta tabela organiza os artigos mais úteis para o projeto de integração **EEG + RV** e consolida a análise da planilha inicial de trabalhos relacionados com a triagem técnico-arquitetural posterior, com foco em três lacunas centrais:

1. camada de comunicação em tempo real entre classificador EEG e engine de RV;
2. uso de **LSL**, sockets, middleware, latência e sincronização;
3. arquitetura de software, além da eficácia clínica.

## Como usar esta tabela

- **Nível de evidência/prioridade**: indica o peso recomendado do artigo no texto.
- **Assunto**: resume o eixo principal do artigo, como BCI, EEG, RV, LSL ou arquitetura.
- **Uso sugerido**: indica onde o artigo encaixa melhor no manuscrito.

## Tabela única consolidada

| Origem | Nível de evidência / prioridade | Ano | Autores | Título | Assunto | Lacuna principal coberta | Uso sugerido | Decisão |
|:--|:--|:--:|:--|:--|:--|:--|:--|:--|
| Planilha inicial | Fundamental | 2021 | Wen, D. et al. | *The Current Research of Combining Multi-Modal Brain-Computer Interfaces With Virtual Reality* | BCI multimodal, RV, estado da arte | Panorama de integração BCI-VR multimodal e tendências recentes | Introdução e base teórica de Trabalhos Relacionados | Manter |
| Planilha inicial | Fundamental | 2022 | Ramadhan, S. et al. | *A Systematic Review of Virtual Reality and Robot Therapy as Recent Rehabilitation Technologies Using EEG-Brain-Computer Interface Based on Movement-Related* | EEG-BCI, RV, robótica, reabilitação | Fundamentação clínica e tecnológica do uso de EEG-BCI em reabilitação | Introdução, Fundamentação Clínica e Trabalhos Relacionados | Manter |
| Planilha inicial | Fundamental | 2021 | Junior, L. F. S. U. et al. | *Brain-Computer Interfaces Systems for Upper and Lower Limb Rehabilitation: A Systematic Review* | BCI, membros superiores e inferiores, reabilitação | Visão geral de sistemas BCI para reabilitação de membros e modalidades de feedback | Introdução e contextualização | Manter |
| Planilha inicial | Complementar | 2025 | He, J. et al. | *Multimodal assessment of a BCI system for stroke rehabilitation integrating motor imagery and motor attempts* | AVC, imagética motora, avaliação multimodal | Evidência clínica recente e métricas para avaliação de sistema BCI em AVC | Metodologia e Discussão | Manter |
| Planilha inicial | Complementar | 2016 | Vourvopoulos, A. et al. | *Motor priming in virtual reality can augment motor-imagery training efficacy in restorative brain-computer interaction* | RV, imagética motora, priming, reabilitação | Justificativa para uso de RV como priming em treinamento por imagética motora | Metodologia e Discussão | Manter |
| Planilha inicial | Complementar | 2019 | Vourvopoulos, A. et al. | *Efficacy and Brain Imaging Correlates of an Immersive Motor Imagery BCI-Driven VR System for Upper Limb Motor Rehabilitation* | BCI-VR imersivo, membro superior, reabilitação | Exemplo aplicado e muito aderente de sistema BCI-VR imersivo para membro superior | Trabalhos Relacionados | Manter |
| Planilha inicial | Complementar | 2021 | Sánchez-Cuesta, F. et al. | *Clinical Effects of Immersive Multimodal BCI-VR Training after Bilateral Neuromodulation with rTMS on Upper Limb Motor Recovery after Stroke* | BCI-VR, rTMS, recuperação motora pós-AVC | Protocolo multimodal avançado para recuperação motora | Discussão e comparação metodológica | Manter |
| Planilha inicial | Complementar | 2023 | Cisotto, G. et al. | *Unraveling Transformative Effects after tDCS and BCI Intervention in Chronic Post-Stroke Patient Rehabilitation* | tDCS, BCI, reabilitação crônica pós-AVC | Comparação de efeitos de terapias combinadas em pacientes crônicos | Discussão | Manter |
| Planilha inicial | Complementar | 2026 | Kokorina, A. et al. | *Case Report: post-stroke rehabilitation with a visuomotor transformation-based brain-computer interface* | BCI visuomotor, reabilitação pós-AVC | Comparação direta com abordagens de transformação visuomotora | Discussão e perspectivas | Manter |
| Planilha inicial | Técnico-arquitetural | 2024 | Lin, K. et al. | *Motor Imagery Performance through Embodied Digital Twins in a Virtual Reality-Enabled BCI Environment* | BCI, RV, digital twin, arquitetura | Base para representação da mão virtual como gêmeo digital incorporado | Arquitetura, Metodologia e Trabalhos Relacionados | Manter |
| IEEE - 1a busca | Essencial | 2018 | Claucich, Carrere e Tabernig | *Virtual Reality Interface Built Using Unity3D for Rehabilitation with BCI Systems Based on Motor Imagery* | BCI, EEG, RV, Unity, reabilitação | Ponte BCI-Unity em reabilitação; comunicação em tempo real; design de interface | Trabalhos Relacionados e Metodologia | Manter |
| IEEE - 1a busca | Essencial | 2022 | Li et al. | *Virtual Reality Roaming System Design Based on Motor Imagery-Based Brain-Computer Interface* | BCI, RV, Unity, imagética motora | Comunicação em tempo real entre plataforma BCI e cena virtual | Trabalhos Relacionados | Manter |
| IEEE - 2a busca | Complementar | 2020 | Xu et al. | *Neurorehabilitation System in Virtual Reality with Low-Cost BCI Devices* | BCI, EEG, RV, reabilitação | BCI + VR + reabilitação em sistema de controle em tempo real | Trabalhos Relacionados | Manter |
| IEEE - 1a busca | Complementar | 2024 | Zhu et al. | *A Human-Centric Metaverse Enabled by Brain-Computer Interface: A Survey* | BCI, RV, metaverso, digital twin | Estado da arte de BCI em ambientes imersivos; desafios de sincronização virtual-físico | Introdução e Estado da Arte | Manter como contextual |
| IEEE - 2a busca | Opcional | 2026 | Vicol, Masic e Mann | *Brain Data Visualization in VR/XR* | EEG, RV/XR, visualização, LSL | Visualização de EEG em VR/XR com streaming | Discussão ou Trabalhos Futuros | Opcional |
| IEEE - 2a busca | Essencial | 2026 | Park et al. | *Toward Practical BCI: A Real-time Wireless Imagined Speech EEG Decoding System* | BCI, EEG, LSL, tempo real, arquitetura | Pipeline ponta a ponta com LSL; streaming contínuo em tempo real | Arquitetura do Sistema e Trabalhos Relacionados | Manter |
| IEEE - 2a busca | Essencial | 2026 | Roque et al. | *Real-Time Mobile EEG Hyperscanning: A Precise and Accessible Platform for Social Brain-Computer Interfaces* | EEG, LSL, sincronização, latência, software | Limites do LSL para sincronização; jitter, drift, latência de software; solução hardware + software | Fundamentação técnica e Discussão metodológica | Manter |
| IEEE - 2a busca | Essencial | 2016 | Wang et al. | *An investigation of triggering approaches for the rapid serial visual presentation paradigm in brain computer interfacing* | BCI, timing, triggers, sincronização | Diferença entre trigger por software e tempo físico real; precisão temporal | Metodologia, sincronização e limitações | Manter |
| IEEE - 2a busca | Essencial | 2025 | Nemes et al. | *Temporal Coupling of Brain Signals and Fine Motor Output Using Affordable EEG* | EEG, LSL, motricidade fina, ambiente virtual | Integração temporal por LSL com precisão de milissegundos; saída motora em ambiente virtual | Trabalhos Relacionados e Metodologia | Manter |
| IEEE - 2a busca | Essencial | 2024 | Kubascik et al. | *BioLab - Application for Online Analysis Using Lab Streaming Layer for Education and Research Purpose* | EEG, LSL, middleware, arquitetura de software | Plataforma/middleware com LSL para streaming, visualização, armazenamento e configuração | Arquitetura de software | Manter |
| IEEE - 2a busca | Complementar | 2019 | Mendonca e Abreu | *A Hybrid System for Assessing Mental Workload* | EEG, eye-tracking, LSL, sincronização | Sincronização multimodal via LSL | Fundamentação técnica | Manter |
| IEEE - 2a busca | Complementar | 2021 | Cannard, Wahbeh e Delorme | *Validating the wearable MUSE headset for EEG spectral analysis and Frontal Alpha Asymmetry* | EEG portátil, LSL, monitoramento | Live-streaming via LSL em EEG portátil | Viabilidade prática / hardware acessível | Manter |
| IEEE - 2a busca | Complementar | 2025 | Orazov et al. | *Optimizing EEG Signal Quality and Streaming Performance in BCIs Using ADS1299EEG-FE* | EEG, aquisição, streaming, latência | Desempenho de aquisição e streaming; estabilidade do sinal e latência baixa | Infraestrutura e aquisição de sinais | Manter |
| IEEE - 2a busca | Reserva | 2024 | S. A.K et al. | *Mind Controlled Movements: Directing Action with Left and Right Thoughts Cooperating with EEG* | EEG, LSL, ML, controle motor | Demonstrador simples com menção a LSL, mas baixo ganho arquitetural | Reserva para consulta pontual | Deixar em reserva |
| IEEE - 2a busca | Reserva | 2026 | Jiang et al. | *A Paradigm for Multi-Attribute Labeling of Targets Based on SSVEP and Eye-Tracking* | BCI, SSVEP, eye-tracking, multimodalidade | Multimodalidade interessante, mas fora do eixo RV + reabilitação motora | Reserva para multimodalidade | Deixar em reserva |
| IEEE - 2a busca | Reserva | 2010 | Ericson, Pallickara e Anderson | *Analyzing Electroencephalograms Using Cloud Computing Techniques* | EEG, computação distribuída, arquitetura | Relevante para computação distribuída, mas distante do recorte atual e antigo | Reserva histórica / técnica | Deixar em reserva |
| IEEE - 2a busca | Descartar | 2025 | Ahangama et al. | *Enhanced Visible Light Communication for Real-Time Audio With Interference-Resilient Protocols* | Comunicação em tempo real, protocolos | Comunicação em tempo real, porém fora do domínio EEG/BCI/RV | Não usar no texto principal | Descartar |
| Artigo-semente | Semente | 2013 | Kothe, C. A.; Makeig, S. | *BCILAB: a platform for brain-computer interface development* | BCI, plataforma, software | Base conceitual de plataforma BCI e ecossistema de desenvolvimento | Fundamentação de plataforma e software | Buscar se faltar base |
| Artigo-semente | Semente | 2018 | Lotte, F. et al. | *A review of classification algorithms for EEG-based brain-computer interfaces: a 10 year update* | EEG, BCI, software, plataformas | Revisão de estado da arte com potencial apoio à discussão de pipelines e plataformas | Estado da arte técnico | Revisitar |
| Artigo-semente | Semente | 2018 | Kerous, B.; Skola, F.; Liarokapis, F. | *EEG-based BCI and video games: a progress report* | BCI, EEG, jogos, Unity/RV | Elo entre BCI, engines interativas e aplicações imersivas | Trabalhos Relacionados e discussão de implementação | Buscar |
| Artigo-semente | Semente | 2017 | Faller, J. et al. | *Regulation of arousal via online neurofeedback improves human performance in a demanding sensory-motor task* | Neurofeedback, tempo real, latência | Reforço para operação online, timing e desempenho em tempo real | Metodologia e discussão técnica | Buscar |

## 5. Recorte Final Recomendado para o Artigo

Se você quiser um conjunto enxuto e forte para citar no texto principal, minha sugestão é:

### Bloco A. EEG + RV + reabilitação

1. Claucich, Carrere e Tabernig (2018)
2. Li et al. (2022)
3. Vourvopoulos et al. (2019)
4. Xu et al. (2020)

### Bloco B. LSL + sincronização + arquitetura

1. Park et al. (2026)
2. Roque et al. (2026)
3. Wang et al. (2016)
4. Nemes et al. (2025)
5. Kubascik et al. (2024)

### Bloco C. Contexto e amarração conceitual

1. Wen et al. (2021)
2. Zhu et al. (2024)
3. Ramadhan et al. (2022)
4. Lotte et al. (2018)

## 6. Síntese Estratégica

O melhor desenho para o artigo é combinar:

- **artigos aplicados** para mostrar que EEG + Unity/VR em reabilitação já é viável;
- **artigos técnicos com LSL e sincronização** para justificar sua arquitetura de comunicação em tempo real;
- **artigos-semente clássicos** para sustentar a discussão metodológica quando a busca mais recente não cobrir toda a base conceitual.

Assim, o capítulo de Trabalhos Relacionados não fica só clínico, nem só descritivo: ele passa a mostrar claramente a ponte entre **neuroreabilitação**, **streaming em tempo real** e **arquitetura de software para integração EEG-RV**.
