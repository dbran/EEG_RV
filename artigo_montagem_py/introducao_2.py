
add_para(doc, "No entanto, a arquitetura de sistemas BCI-VR apresenta desafios críticos de interoperabilidade que "
              "limitam sua disseminação e replicabilidade em contextos de saúde reais. Tipicamente, dois softwares "
              "independentes devem comunicar-se em tempo real: o software BCI, responsável pela aquisição, pré-processamento "
              "e classificação de sinais neurais, e o software VR, encarregado da renderização do ambiente virtual e do "
              "feedback sensorial (LOTTE et al., 2012). A maioria das implementações documentadas recorre a protocolos de "
              "comunicação ad hoc, frequentemente baseados em sockets TCP/UDP proprietários, que dificultam a manutenção, "
              "escalabilidade e portabilidade entre diferentes plataformas de hardware e engines gráficas (WOO et al., 2021; "
              "HAL, 2023).")

add_para(doc, "A ausência de uma camada de abstração padronizada — um middleware — obriga pesquisadores e "
              "desenvolvedores a reimplementar rotinas de comunicação para cada nova configuração experimental, "
              "aumentando exponencialmente a complexidade de desenvolvimento e o tempo de deployment (LOTTE et al., 2012). "
              "Em aplicações de neuroreabilitação, a latência total do sistema — desde a aquisição do sinal EEG até a "
              "renderização do feedback visual — deve permanecer abaixo de 300 milissegundos para garantir a coerência "
              "perceptivo-motora e a eficácia terapêutica (LI et al., 2025). Um middleware otimizado pode reduzir "
              "significativamente os atrasos de processamento e transmissão, implementando buffers circulares, mecanismos "
              "de predição e estratégias de compressão de dados (HAL, 2023).")

add_para(doc, "Além disso, do ponto de vista da gestão em saúde, a replicabilidade e o baixo custo de implantação "
              "são determinantes para a viabilidade de escala no SUS. Soluções proprietárias (ex: OpenViBE com plugins "
              "comerciais, engines VR licenciadas) impõem barreiras econômicas e legais que inviabilizam a adoção em "
              "larga escala (BAHIA et al., 2020). Um middleware open-source, modular e multiplataforma representa uma "
              "alternativa estratégica para democratizar o acesso à neuroreabilitação tecnológica no Brasil.")

add_title(doc, "1.1.3 A Integração BCI-VR como Solução e o Papel do Middleware")

add_para(doc, "A integração de BCI com VR imersiva emerge como abordagem inovadora com potencial transformador "
              "na neuroreabilitação de pacientes pós-AVE. A VR oferece ambientes controlados, seguros e customizáveis "
              "para treinamento motor, com feedback multimodal (visual, auditivo, háptico) que pode ser adaptado às "
              "necessidades individuais do paciente e ao estágio de recuperação (LECUYER et al., 2008; PISZCZ et al., 2024). "
              "Quando combinada com BCI baseado em imagética motora, a VR permite que o paciente visualize, em tempo real, "
              "a sua intenção motora decodificada como movimento de uma mão virtual — mesmo quando a via motora periférica "
              "está comprometida e não permite movimento físico efetivo (VOURVOPOULOS et al., 2013). Esse feedback "
              "visual imediato potencializa o efeito de priming motor e a reorganização cortical, acelerando a recuperação "
              "funcional (VOURVOPOULOS; BERMÚDEZ I BADIA, 2016).")

add_para(doc, "No entanto, a realização dessa integração exige uma camada de software intermediária — o middleware — "
              "que traduza, em tempo real, os comandos neurais decodificados em movimentos cinemáticos de alta fidelidade "
              "no ambiente virtual (LOTTE et al., 2012). O middleware deve: (i) receber as mensagens de classificação do "
              "sistema BCI (no caso, mensagens JSON geradas por um classificador CNN/LM de EEG); (ii) converter os campos "
              "probabilísticos dessas mensagens (probabilidades de classe, estados de movimento, thresholds) em parâmetros "
              "cinemáticos contínuos de articulação da mão (posição, orientação, velocidade e aceleração de 25 juntas); "
              "(iii) sincronizar temporalmente esses parâmetros com o framerate da engine de VR; e (iv) transmiti-los para "
              "a renderização imersiva no headset VR (HAL, 2023).")

add_para(doc, "A sincronia temporal é particularmente crítica. Quando o paciente imagina o movimento de abrir a mão, "
              "a mão virtual deve abrir-se o mais próximo possível, no tempo, da intenção neural. Latências excessivas "
              "(superiores a 300 ms) ou jitter (variação irregular da latência) comprometem a ilusão de propriedade "
              "corporal — a percepção de que a mão virtual pertence ao próprio paciente — e podem induzir ciberenjoo "
              "(cybersickness), reduzindo a adesão terapêutica (LI et al., 2025). O desafio, portanto, não é apenas "
              "transmitir dados, mas garantir que a tradução de intenção neural em movimento virtual seja fluida, "
              "previsível e coerente com a experiência sensorial do paciente.")

add_para(doc, "Do ponto de vista da gestão em saúde, o middleware open-source representa uma infraestrutura "
              "compartilhada que reduz o custo de desenvolvimento e manutenção de sistemas BCI-VR. Em vez de cada "
              "instituição reimplementar a comunicação entre BCI e VR, uma camada padronizada e documentada permite "
              "que pesquisadores e desenvolvedores foquem na inovação clínica — protocolos de intervenção, personalização "
              "terapêutica, avaliação de resultados — em vez da engenharia de software de baixo nível (WOO et al., 2021). "
              "Isso é especialmente relevante para o SUS, onde recursos são escassos e a replicabilidade de soluções "
              "tecnológicas é determinante para o impacto em saúde pública (MINISTÉRIO DA SAÚDE, 2022).")

print("Seções 1.1.2 (continuação) e 1.1.3 criadas.")