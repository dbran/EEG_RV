
# ============================================
# 2 REFERENCIAL TEÓRICO - Completo com citações
# ============================================

add_title(doc, "2 REFERENCIAL TEÓRICO")
add_para(doc, "")

add_title(doc, "2.1 Acidente Vascular Encefálico: Fisiopatologia, Sequelas e Reabilitação Neuromotora")

add_para(doc, "O acidente vascular encefálico (AVE) resulta da interrupção súbita do fluxo sanguíneo cerebral, seja por "
              "obstrução vascular (AVE isquêmico, aproximadamente 85% dos casos) ou ruptura de vaso (AVE hemorrágico, "
              "aproximadamente 15%). A isquemia cerebral aguda desencadeia cascata neuroquímica de excitotoxicidade, "
              "estresse oxidativo e inflamação, culminando em morte neuronal e perda de função nos territórios vasculares "
              "afetados (FEIGIN et al., 2022). A mortalidade no primeiro ano pós-AVE varia entre 30% e 50%, e entre os "
              "sobreviventes, a incapacidade funcional permanente é a regra mais do que a exceção (GBD 2019 STROKE "
              "COLLABORATORS, 2021).")

add_para(doc, "A hemiparesia — fraqueza unilateral do corpo contralateral à lesão — é a sequela motora mais frequente, "
              "decorrente do comprometimento da via corticoespinhal. A mão e o punho são particularmente afetados devido "
              "à representação cortical extensa e à complexidade da motricidade fina (LAWRENCE et al., 2001). A Escala de "
              "Fugl-Meyer (FM-UE) é o instrumento gold-standard para avaliação da função motora de membro superior pós-AVE, "
              "variando de 0 (paralisia completa) a 66 (função normal), sendo que a maioria dos pacientes se situa na faixa "
              "de moderada a severa incapacidade nos primeiros meses (FUGL-MEYER et al., 1975).")

add_para(doc, "A teoria da plasticidade cerebral fundamenta a reabilitação neuromotora: o cérebro adulto mantém capacidade "
              "de reorganização sináptica e cortical em resposta à lesão e ao treinamento (KLEIM; JONES, 2008). Princípios "
              "neurofisiológicos críticos incluem: (i) uso dependente — áreas neurais subutilizadas sofrem atrofia, enquanto "
              "áreas treinadas se fortalecem; (ii) especificidade da prática — a recuperação é específica aos movimentos "
              "treinados; (iii) intensidade — maior número de repetições correlaciona-se com melhores resultados; e (iv) "
              "feedback saliente — informação sensorial relevante potencializa o aprendizado motor (ZEILER; KRASCHI, 2013). "
              "No entanto, quando a via motora está severamente comprometida, o paciente não consegue executar movimentos "
              "voluntários mesmo com assistência máxima, inviabilizando a aplicação dos princípios de uso dependente e prática "
              "específica (DIETRICH, 2021).")

add_para(doc, "É neste cenário que as BCIs baseadas em imagética motora oferecem uma via alternativa: permitindo que o "
              "paciente pratique a intenção motora — com feedback visual da mão virtual se movendo conforme sua imaginação — "
              "mesmo sem capacidade de movimento físico efetivo, induzindo reorganização cortical premotora e sensorimotora "
              "(WOLPAW et al., 2002; PFURTSCHELLER; LOPES DA SILVA, 1999). Essa abordagem é particularmente relevante para "
              "o SUS brasileiro, onde a escassez de terapeutas e a concentração geográfica dos serviços de reabilitação limitam "
              "o acesso de milhares de pacientes (MINISTÉRIO DA SAÚDE, 2022).")

add_title(doc, "2.2 Interfaces Cérebro-Computador e Imagética Motora na Reabilitação pós-AVE")

add_para(doc, "As interfaces cérebro-computador (BCIs) são sistemas que traduzem a atividade neural do usuário em comandos "
              "para dispositivos externos, estabelecendo um canal de comunicação direto e independente das vias motoras e "
              "musculares convencionais (WOLPAW et al., 2002). Em reabilitação neuromotora, as BCIs exploram o princípio de "
              "neurofeedback motor: o paciente modula intencionalmente seus padrões neurais sensorimotores e recebe feedback "
              "imediato da decodificação, reforçando os circuitos neurais comprometidos (PFURTSCHELLER; LOPES DA SILVA, 1999; "
              "PFURTSCHELLER; ARANIBAR, 1979).")

add_para(doc, "A imagética motora (Motor Imagery – MI) consiste na imaginação mental de movimentos corporais — como abrir "
              "e fechar a mão ou rotacionar o punho — sem a execução física efetiva. Durante a MI, observa-se a modulação das "
              "oscilações rítmicas nas bandas de frequência mu (8-13 Hz) e beta (13-30 Hz) sobre as áreas sensorimotoras, "
              "fenômeno denominado desincronização evento-relacionada (ERD) e sincronização evento-relacionada (ERS) "
              "(PFURTSCHELLER; ARANIBAR, 1979). A detecção e classificação desses padrões neurais permitem traduzir a intenção "
              "motora do paciente em comandos computacionais (PFURTSCHELLER; LOPES DA SILVA, 1999).")

add_para(doc, "Meta-análises recentes demonstram que a terapia BCI associada à reabilitação convencional produz ganhos "
              "funcionais superiores à reabilitação isolada, particularmente em subagudos e crônicos pós-AVE, com efeitos "
              "sustentados em follow-up de 6 meses (CARAMIA et al., 2021; ANG et al., 2015). No entanto, a generalização "
              "dos resultados para a prática clínica rotineira permanece limitada por barreiras tecnológicas: complexidade de "
              "operação, alto custo, latência excessiva e falta de interoperabilidade entre componentes (BONINGER et al., 2014). "
              "A tradução de comandos neurais discretos em movimentos contínuos de alta fidelidade no ambiente virtual — tarefa "
              "da camada de middleware — é um desses gargalos críticos (LOTTE et al., 2012).")

add_title(doc, "2.3 Redes Neurais Convolucionais para Decodificação de Intenção Motora")

add_para(doc, "O advento do aprendizado profundo revolucionou a classificação de sinais de EEG. Schirrmeister et al. (2017) "
              "demonstraram empiricamente que redes convolucionais rasas e profundas superam substancialmente métodos tradicionais "
              "(CSP + LDA/SVM) na classificação de MI-EEG, tanto em termos de acurácia quanto de robustez a variações "
              "inter-sujeito. Lawhern et al. (2018) propuseram o EEGNet, arquitetura compacta que combina convoluções temporais "
              "e espaciais com convoluções separáveis (depthwise separable convolutions), projetada especificamente para datasets "
              "de treinamento limitados — condição típica em BCI clínico, onde a coleta de dados é onerosa e cansativa para os "
              "pacientes.")

add_para(doc, "Variações e extensões do EEGNet incluem: MI-EEGNet (RIYAD et al., 2021), que incorpora blocos inception "
              "para extração multiescala de características temporais e espaciais; EEG-ITNet (SALAMI et al., 2022), que emprega "
              "convoluções temporais inception com camadas de explicabilidade; e AMEEGNet (2025), que integra mecanismos de "
              "atenção multiescala. Para o presente projeto, o classificador CNN/LM desenvolvido pelo colega na tese de doutorado "
              "gera mensagens JSON com campos probabilísticos (p_combined, ema, p_move, label) que alimentam a camada de "
              "tradução deste mestrado (MOVING DATASET, 2024).")

add_title(doc, "2.4 Realidade Virtual Imersiva em Neuroreabilitação")

add_para(doc, "A realidade virtual (VR) oferece ambientes controlados, seguros e customizáveis para treinamento motor, com "
              "feedback multimodal (visual, auditivo, háptico) que pode ser adaptado às necessidades individuais do paciente e "
              "ao estágio de recuperação (LECUYER et al., 2008). Estudos demonstram que a integração BCI-VR potencializa o efeito "
              "de priming motor — a ativação subliminar de circuitos neurais motores — e a reorganização cortical em pacientes "
              "pós-AVE (VOURVOPOULOS et al., 2013; VOURVOPOULOS; BERMÚDEZ I BADIA, 2016).")

add_para(doc, "Engines de VR como Unity e Unreal Engine dominam o mercado de desenvolvimento de aplicações imersivas. "
              "Ambos oferecem suporte nativo a hand tracking (rastreamento de mão) através de APIs como OpenXR, Meta XR SDK "
              "e Ultraleap (META, 2026; HTC VIVE, 2024). A representação da mão em VR emprega tipicamente modelos esqueléticos "
              "com 25 juntas articuladas, parametrizadas por posição tridimensional (x, y, z), orientação (quaternion ou ângulos de "
              "Euler) e derivadas cinemáticas (velocidade angular, aceleração linear). A precisão do hand tracking é fundamental "
              "para a credibilidade da experiência imersiva e para a eficácia do feedback terapêutico (LI et al., 2025).")

add_para(doc, "A imersão e o senso de presença são determinantes para a eficácia terapêutica: quando o paciente percebe a mão "
              "virtual como própria (ilusão de propriedade corporal), o feedback neural é potencializado. Latências excessivas "
              "(superiores a 300 ms) ou erros de tracking comprometem essa ilusão e podem induzir ciberenjoo (cybersickness), "
              "reduzindo a adesão terapêutica (LI et al., 2025). A sincronia temporal entre a intenção neural (recebida via JSON) "
              "e o movimento da mão virtual (renderizado na engine) é, portanto, um requisito crítico que depende diretamente da "
              "qualidade da camada de tradução e sincronização.")

add_title(doc, "2.5 Protocolos de Comunicação e Sincronização Temporal em Sistemas BCI-VR")

add_para(doc, "O conceito de middleware em sistemas BCI-VR foi formalizado por Lotte et al. (2012), que propuseram uma "
              "arquitetura em três camadas: (i) componente BCI para aquisição e classificação de sinais; (ii) middleware para "
              "roteamento e tradução de comandos; (iii) sistema VR para renderização e feedback. Implementações concretas incluem "
              "RehabNet (VOURVOPOULOS et al., 2013), arquitetura distribuída para neuroreabilitação motora e cognitiva utilizando "
              "VRPN como protocolo de comunicação; NeuRow (VOURVOPOULOS; BERMÚDEZ I BADIA, 2016), ambiente VR imersivo para "
              "MI-BCI com remo remoto, integrando OpenViBE e Unity; e sistema SSVEP-AR (HAL, 2023), middleware como autômato "
              "de estados finitos em Python, comunicando BCI (OpenViBE), sistema AR (Unity) e plataforma de automação residencial.")

add_para(doc, "O padrão VRPN (Virtual Reality Peripheral Network), proposto por Taylor et al. (2001), oferece abstração de "
              "dispositivos de VR, mas apresenta limitações para streaming de dados de alta frequência e baixa latência. Protocolos "
              "mais recentes, como o Lab Streaming Layer (LSL), ganham tração por sua capacidade de multiplexação de múltiplos "
              "streams temporais com sincronização por timestamps de alta precisão (GORMAN et al., 2021). No entanto, o LSL é um "
              "protocolo de transporte — não uma arquitetura de middleware completa. Não define interfaces de conversão cinemática, "
              "não abstrai engines VR, e não oferece mecanismos de predição de estado ou otimização para renderização em tempo real.")

add_para(doc, "A sincronização temporal em sistemas distribuídos BCI-VR envolve desafios específicos: jitter (variação "
              "irregular da latência de pacotes), drift de relógio entre componentes, perda de pacotes em redes sem fio, e "
              "diferenças de framerate entre processamento neural (tipicamente 10-50 Hz) e renderização VR (90 Hz ou mais). "
              "Mecanismos de compensação incluem: buffers circulares com timestamps, interpolação de estados intermediários, "
              "predição de movimento por dead reckoning, e rate limiting adaptativo (HAL, 2023; GORMAN et al., 2021). "
              "Nenhuma solução existente integra especificamente a tradução de mensagens JSON probabilísticas de classificadores "
              "CNN para parâmetros cinemáticos contínuos de hand tracking em engines VR, com análise de viabilidade de implantação "
              "em saúde pública — lacuna que o presente projeto pretende preencher.")

page_break(doc)
print("Referencial Teórico completo finalizado.")