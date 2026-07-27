
add_title(doc, "1.1.4 O Grupo NERV e a Delimitação do Escopo deste Mestrado")

add_para(doc, "O presente trabalho insere-se no projeto de pesquisa macro 'Sistema integrado de BCI, realidade "
              "virtual imersiva e robótica para reabilitação neuromotora da mão pós-AVE', desenvolvido pelo Grupo de "
              "Pesquisa NERV (Neuroengineering and Rehabilitation Virtual) da Universidade Federal de Ciências da Saúde "
              "de Porto Alegre (UFCSPA). O NERV é um grupo interdisciplinar dedicado ao desenvolvimento de tecnologias "
              "assistivas e de reabilitação baseadas em engenharia neural, realidade virtual e robótica, com foco em "
              "condições neurológicas adquiridas, particularmente o AVE.")

add_para(doc, "A arquitetura do sistema integrado NERV compreende quatro subsistemas interdependentes: (1) "
              "Subsistema Neural (BCI), responsável pela aquisição de EEG (OpenBCI / g.tec), pré-processamento de sinais, "
              "e classificação da intenção motora via rede neural convolucional / modelo de linguagem (CNN/LM), gerando "
              "mensagens JSON com probabilidades de classe, estados de movimento e parâmetros de configuração; (2) "
              "Subsistema de Tradução e Sincronização — objeto do presente mestrado — que recebe as mensagens JSON, "
              "converte seus campos probabilísticos em parâmetros cinemáticos contínuos de articulação da mão, e sincroniza "
              "temporalmente esses parâmetros com a engine de VR; (3) Subsistema Imersivo (VR), desenvolvido em engine Unity, "
              "que renderiza a mão virtual no headset VR e fornece feedback visual/auditivo ao paciente; e (4) Subsistema "
              "Robótico, desenvolvido na tese de doutorado do colega [Nome], compreendendo exoesqueleto de mão (impressão 3D / "
              "atuadores), feedback háptico e assistência mecânica, com sincronização com avatar VR.")

add_para(doc, "Enquanto a tese de doutorado de [Nome do Colega] desenvolve o classificador neural (CNN/LM) que "
              "decodifica os sinais de EEG em comandos discretos — gerando mensagens JSON com campos como type, label, "
              "p_combined, ema, p_move, threshold, sfreq, n_channels —, o presente mestrado foca especificamente na "
              "camada de tradução e sincronização temporal: receber essas mensagens JSON via protocolo de comunicação em "
              "tempo real (ZeroMQ/WebSocket), validar e filtrar seus campos (incluindo detecção de rejeição via campo rejected), "
              "converter os campos probabilísticos em parâmetros cinemáticos contínuos de 25 juntas da mão virtual "
              "(posição, orientação, velocidade e aceleração), e transmiti-los à engine Unity para renderização imersiva "
              "no headset VR (Meta Quest), com latência mínima e máxima coerência perceptivo-motora.")

add_para(doc, "Esta delimitação é intencional e estratégica: a camada de tradução constitui o gargalo tecnológico "
              "crítico que, se não resolvido com robustez, eficiência e baixo custo, inviabiliza a escalabilidade e "
              "replicabilidade do sistema completo em contextos clínicos reais. Sem uma camada de abstração padronizada, "
              "cada nova implantação do sistema NERV demandaria reengenharia completa da comunicação entre o classificador "
              "e a engine VR, tornando inviável a disseminação em hospitais, ambulatórios e centros de reabilitação do SUS. "
              "A contribuição específica deste mestrado, portanto, é tecnológica e de gestão em saúde: desenvolver uma "
              "infraestrutura de software reutilizável, documentada e de baixo custo que habilite a tradução clínica do "
              "sistema NERV e de outros sistemas BCI-VR semelhantes.")

add_title(doc, "1.2 Questão de Pesquisa")

add_para(doc, "Como desenvolver uma camada de software em Python que receba mensagens JSON geradas por um "
              "classificador CNN/LM de eletroencefalografia (EEG), converta seus campos probabilísticos (p_combined, "
              "ema, p_move, label, threshold) em parâmetros cinemáticos contínuos de articulação da mão virtual, e os "
              "transmita à engine Unity para renderização sincronizada no headset de realidade virtual, garantindo latência "
              "inferior a 150 ms, jitter controlado e coerência perceptivo-motora em cenários de reabilitação neuromotora "
              "pós-acidente vascular encefálico, de forma viável para implantação em cenários de saúde pública e privada "
              "no Brasil?")

add_title(doc, "1.3 Objetivos")
add_title(doc, "1.3.1 Objetivo Geral")

add_para(doc, "Desenvolver e validar uma camada de software de tradução e sincronização temporal que receba mensagens "
              "JSON de classificação neural (CNN/LM) de EEG, converta seus campos probabilísticos em parâmetros "
              "cinemáticos contínuos de articulação da mão virtual, e os transmita à engine Unity para renderização "
              "sincronizada no headset de realidade virtual, permitindo a projeção precisa e de baixa latência do movimento "
              "de mão em ambientes imersivos de reabilitação neuromotora pós-acidente vascular encefálico.")

add_title(doc, "1.3.2 Objetivos Específicos")

objetivos = [
    "1. Especificar o schema de mensagens JSON e o protocolo de comunicação entre o classificador CNN/LM e a camada de "
    "tradução, considerando campos como type, label, p_combined, ema, p_move, threshold, sfreq, n_channels, rejected;",
    
    "2. Implementar módulo de parsing e filtragem das mensagens JSON em Python, incluindo validação de schema, "
    "filtro de média móvel exponencial (EMA), detecção de rejeição (campo rejected) e tratamento de valores nulos;",
    
    "3. Desenvolver algoritmo de conversão probabilístico-cinemática contínua que mapeie os campos p_combined, "
    "ema e p_move em parâmetros de 25 juntas da mão virtual (posição, orientação, velocidade, aceleração);",
    
    "4. Implementar mecanismos de sincronização temporal (buffer circular com timestamps, interpolação de estados, "
    "predição de movimento por dead reckoning, compensação de jitter) para minimizar latência e maximizar fluidez;",
    
    "5. Integrar a camada de tradução com a engine Unity via protocolo de comunicação em tempo real, renderizando "
    "o movimento da mão virtual no headset VR (Meta Quest) com sincronia ao framerate da engine;",
    
    "6. Avaliar funcionalmente a sincronia temporal entre recepção do JSON e movimento renderizado, com métricas "
    "de latência end-to-end, jitter, drift temporal e correlação JSON-movimento, em cenário de imagética motora;",
    
    "7. Realizar análise de custo-efetividade comparativa entre a camada open-source proposta e soluções proprietárias, "
    "projetando cenários de implantação no SUS e na saúde suplementar."
]

for obj in objetivos:
    add_para(doc, obj)

print("Seções 1.1.4, 1.2 e 1.3 criadas.")