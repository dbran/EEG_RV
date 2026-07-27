
# ============================================
# 3 TRABALHOS RELACIONADOS - Completo com citações
# ============================================

add_title(doc, "3 TRABALHOS RELACIONADOS")
add_para(doc, "")

add_title(doc, "3.1 Arquiteturas de Middleware para Integração BCI-VR")

add_para(doc, "O middleware é a camada de software crítica que viabiliza a comunicação em tempo real entre sistemas de "
              "aquisição e processamento de sinais neurais (BCI) e engines de realidade virtual (VR). Sua ausência ou inadequação "
              "impõe barreiras de interoperabilidade que limitam a replicabilidade e escalabilidade de soluções de neuroreabilitação "
              "em contextos clínicos reais (LOTTE et al., 2012). A revisão sistemática da literatura revela que, embora existam "
              "componentes isolados maduros (classificadores CNN, engines VR, protocolos de comunicação), falta a camada de "
              "abstração — o middleware — que os integre de forma coesa, eficiente e economicamente viável para reabilitação "
              "neuromotora (HAL, 2023).")

add_para(doc, "RehabNet (Vourvopoulos et al., 2013) foi uma das primeiras arquiteturas distribuídas voltadas especificamente "
              "para neuroreabilitação motora e cognitiva. O sistema utiliza o protocolo VRPN (Virtual Reality Peripheral Network) "
              "para comunicação entre componentes BCI e VR, demonstrando a viabilidade de arquiteturas modulares. No entanto, "
              "o RehabNet apresenta limitações significativas para o escopo do presente projeto: não contempla classificadores "
              "baseados em deep learning (CNNs), não oferece suporte a hand tracking detalhado de mão (limitando-se a interações "
              "genéricas de navegação), e utiliza VRPN — protocolo com overhead de latência inadequado para streaming de dados "
              "cinemáticos de alta frequência (90 Hz) (TAYLOR et al., 2001).")

add_para(doc, "NeuRow (Vourvopoulos; Bermúdez i Badia, 2016) expandiu a integração BCI-VR para ambientes imersivos de remo "
              "remoto, integrando OpenViBE (processamento de sinais) e Unity (renderização VR). Embora represente avanço em termos "
              "de imersão, a arquitetura apresenta latência não otimizada para aplicações de alta precisão motora, e a comunicação "
              "entre componentes é baseada em sockets TCP proprietários, dificultando a portabilidade entre engines e a substituição "
              "de classificadores. Além disso, o NeuRow não contempla a tradução de comandos probabilísticos contínuos em parâmetros "
              "cinemáticos de articulação da mão, limitando-se a comandos discretos de navegação.")

add_para(doc, "Sistema SSVEP-AR (HAL, 2023) propôs um middleware implementado como autômato de estados finitos em Python, "
              "comunicando BCI (OpenViBE), sistema de realidade aumentada (Unity) e plataforma de automação residencial via sockets "
              "TCP. O trabalho demonstra a viabilidade de arquiteturas de estados para BCI-VR/AR, porém é limitado a um único engine "
              "(Unity), a um paradigma BCI específico (SSVEP — potenciais evocados visualmente, não imagética motora), e não contempla "
              "hand tracking nem análise de custo-efetividade para saúde pública. A tradução de mensagens de classificação em "
              "movimentos cinemáticos contínuos não é abordada.")

add_para(doc, "Lab Streaming Layer (LSL) (Gorman et al., 2021) emerge como protocolo de comunicação de referência na comunidade "
              "BCI, oferecendo multiplexação de múltiplos streams temporais com sincronização por timestamps de alta precisão. "
              "Diferentemente de VRPN, o LSL foi projetado para neurofisiologia, com overhead mínimo e latência sub-milissegundo. "
              "No entanto, o LSL é um protocolo de transporte — não uma arquitetura de middleware completa. Não define interfaces de "
              "conversão cinemática, não abstrai engines VR, e não oferece mecanismos de predição de estado ou otimização para "
              "renderização em tempo real. A integração de LSL com conversão probabilístico-cinemática e sincronização temporal "
              "específica para hand tracking em VR permanece inexplorada na literatura.")

add_para(doc, "A Tabela 3 sintetiza a comparação entre as arquiteturas middleware existentes e a proposta do presente projeto.")

add_para(doc, "Tabela 3 – Comparação de arquiteturas middleware em sistemas BCI-VR")

add_para(doc, "Característica | RehabNet (2013) | NeuRow (2016) | SSVEP-AR (2023) | LSL (2021) | Proposta deste projeto")
add_para(doc, "Paradigma BCI | MI genérica | MI | SSVEP | Qualquer | MI (CNN/LM JSON)")
add_para(doc, "Formato de entrada | Sinais brutos | Sinais brutos | Sinais brutos | Streams temporais | Mensagens JSON probabilísticas")
add_para(doc, "Conversão cinemática contínua | Não | Não | Não | Não | Sim (25 juntas)")
add_para(doc, "Hand tracking detalhado | Não | Não | Não | Não | Sim (Unity + Meta Quest)")
add_para(doc, "Engines VR suportadas | Unity | Unity | Unity | Qualquer | Unity (extensível)")
add_para(doc, "Protocolo de comunicação | VRPN | TCP proprietário | TCP (Python) | LSL | LSL + ZeroMQ/WebSocket")
add_para(doc, "Latência reportada | Não reportada | ~200 ms | ~150 ms | Sub-ms (transporte) | <150 ms (meta)")
add_para(doc, "Sincronização temporal | Não | Não | Não | Timestamps | Buffer + interpolação + predição")
add_para(doc, "Análise de custo-efetividade | Não | Não | Não | Não | Sim (SUS/suplementar)")
add_para(doc, "Licenciamento | Não especificado | Não especificado | Não especificado | Open-source | Open-source (MIT/Apache)")
add_para(doc, "Aplicação clínica | Reabilitação motora/cognitiva | Remo remoto | Automação residencial | Pesquisa genérica | Reabilitação mão pós-AVE")

add_para(doc, "A lacuna identificada é clara: não existe middleware open-source, de baixa latência, com conversão cinemática "
              "contínua integrada, que receba mensagens JSON probabilísticas de classificadores CNN/LM de EEG e as traduza em "
              "parâmetros de hand tracking detalhado em engines VR, acompanhado de análise de viabilidade econômica para implantação "
              "em sistemas de saúde. O presente projeto preenche essa lacuna.")

add_title(doc, "3.2 Classificadores de EEG e Deep Learning (Contexto Tecnológico)")

add_para(doc, "A precisão da camada de tradução depende fundamentalmente da qualidade dos comandos de entrada provenientes "
              "do classificador BCI. Schirrmeister et al. (2017) estabeleceram as bases para aplicação de CNNs em EEG, demonstrando "
              "superioridade sobre métodos clássicos (CSP + LDA/SVM). Lawhern et al. (2018) propuseram o EEGNet, arquitetura compacta "
              "que se tornou padrão de fato na área. Riyad et al. (2021) e Salami et al. (2022) estenderam o EEGNet com mecanismos de "
              "atenção e explicabilidade. O dataset MOVING (2024) oferece dados multimodais de EEG e hand tracking, recurso essencial "
              "para o treinamento do pipeline proposto. No entanto, esses trabalhos focam exclusivamente na classificação — não na "
              "integração em tempo real com sistemas VR. A saída do classificador (mensagens JSON com campos probabilísticos) é o "
              "ponto de partida da camada de tradução desenvolvida neste mestrado.")

add_title(doc, "3.3 Hand Tracking e Engines VR (Contexto Tecnológico)")

add_para(doc, "Unity e Unreal Engine dominam o mercado de desenvolvimento VR, oferecendo APIs nativas de hand tracking "
              "(Meta XR SDK, OpenXR, Ultraleap) com modelos esqueléticos de 25 juntas (META, 2026; HTC VIVE, 2024). A integração "
              "desses sistemas com comandos derivados de BCI, mediada por camada de tradução otimizada, permanece subexplorada na "
              "literatura. A maioria das aplicações BCI-VR utiliza interações simplificadas (seleção de objetos, navegação), não "
              "projeção contínua de movimento de mão com fidelidade cinemática. A tradução de probabilidades de classe em parâmetros "
              "articulares contínuos, com sincronia temporal ao framerate da engine, é o desafio específico abordado pelo presente projeto.")

add_title(doc, "3.4 Síntese da Lacuna")

add_para(doc, "A revisão sistemática revela que, embora existam componentes isolados maduros (classificadores CNN, engines VR, "
              "protocolos de comunicação), falta a camada de abstração — o middleware de tradução e sincronização — que os integre "
              "de forma coesa, eficiente e economicamente viável para reabilitação neuromotora. O presente projeto não propõe apenas "
              "mais um middleware genérico, mas uma arquitetura específica para o domínio clínico da reabilitação pós-AVE, com "
              "requisitos de latência, sincronia temporal, custo e usabilidade definidos pelo contexto de saúde. A contribuição "
              "central é a tradução de mensagens JSON probabilísticas de classificação neural em movimentos cinemáticos contínuos de "
              "alta fidelidade da mão virtual, com máxima sincronia temporal e viabilidade de implantação em sistemas de saúde pública.")

page_break(doc)
print("Trabalhos Relacionados completos finalizados.")