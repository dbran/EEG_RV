# ============================================
# 4 MATERIAIS E MÉTODOS
# ============================================
add_title(doc, "4 MATERIAIS E MÉTODOS")
add_para(doc, "")

add_title(doc, "4.1 Método de Pesquisa e Delineamento")
add_para(doc, "A presente pesquisa classifica-se como pesquisa aplicada de natureza tecnológica, com abordagem experimental e delineamento quase-experimental para a fase de validação com participantes. O método engloba as fases de especificação arquitetural, implementação de software, integração de componentes e avaliação de desempenho. Adicionalmente, será realizada análise de custo-efetividade comparativa entre a camada de tradução proposta e soluções proprietárias, utilizando método de análise de decisão em saúde (cost-effectiveness analysis) (DRUMMOND et al., 2015).")

add_title(doc, "4.2 Arquitetura da Camada de Tradução e Sincronização")
add_para(doc, "A camada de software será implementada em Python 3.10+, arquitetada em módulos desacoplados com comunicação via filas de mensagens assíncronas (asyncio). A arquitetura compreende quatro módulos principais: (1) Módulo de Recepção JSON, responsável pelo parsing e validação de schema das mensagens recebidas via ZeroMQ ou WebSocket; (2) Módulo de Filtragem e Estado, que aplica filtro de média móvel exponencial (EMA), detecta rejeições (campo rejected) e mantém estado consistente entre mensagens; (3) Módulo de Conversão Cinemática, que mapeia campos probabilísticos (p_combined, ema, p_move, label) em parâmetros de 25 juntas da mão virtual (posição, orientação quaternion, velocidade angular, aceleração linear); e (4) Módulo de Transmissão Unity, que serializa os parâmetros cinemáticos no formato nativo da engine e os transmite via UDP local ou memória compartilhada.")

add_title(doc, "4.3 Schema JSON e Protocolo de Comunicação")
add_para(doc, "O schema de entrada segue o formato estabelecido pelo classificador CNN/LM da tese do colega [Nome], com duas mensagens principais: (a) Mensagem de configuração: {'type': 'started', 'sim': bool, 'mode': str, 'modality': str, 'threshold': float, 'group_id': int, 'sfreq': float, 'n_channels': int, 'hand_connected': Optional[bool]}; e (b) Mensagem de inferência: {'type': 'inference', 'label': int, 'label_text': str, 'p_combined': List[float], 'ema': List[float], 'raw_pred': int, 'rejected': bool, 'reason': str, 'is_mi': bool, 'p_move': float, 'tau': float, 'consecutive_rejected': int, 'group_id': int, 'hand': Optional[Any]}. O protocolo de transporte será ZeroMQ (padrão pub-sub) com fallback para WebSocket, garantindo latência sub-milissegundo na camada de transporte (GORMAN et al., 2021).")

add_title(doc, "4.4 Algoritmo de Conversão Probabilístico-Cinemática")
add_para(doc, "O algoritmo de conversão mapeia os campos probabilísticos da mensagem JSON em parâmetros cinemáticos contínuos de 25 juntas da mão virtual. Para cada mensagem de inferência: (1) Se rejected=True, mantém estado anterior com decaimento exponencial; (2) Se label=0 (SEM MOVIMENTO), aplica pose neutra com relaxamento suave; (3) Se label>0, interpola entre poses-chave pré-definidas (abertura, fechamento, pinça) ponderadas por p_combined e ema; (4) Aplica suavização por filtro de Kalman ou EMA no espaço de juntas; (5) Gera velocidades e acelerações por derivação numérica com regularização. O mapeamento é calibrado por sujeito via coleta de dados de hand tracking real (MOVING DATASET, 2024).")

add_title(doc, "4.5 Mecanismos de Sincronização Temporal")
add_para(doc, "Para garantir sincronia entre recepção do JSON (tipicamente 10-50 Hz) e renderização VR (90 Hz), implementam-se: (1) Buffer circular com timestamps de alta precisão (time.monotonic_ns); (2) Interpolação de estados intermediários por splines cúbicas ou SLERP para quaternions; (3) Predição de estado por dead reckoning quando há gap de pacotes; (4) Compensação de drift de relógio entre processos via NTP/PTP; (5) Rate limiting adaptativo que descarta ou interpola estados conforme carga da engine. O target de jitter é <5 ms (desvio padrão da latência) (LI et al., 2025).")

add_title(doc, "4.6 Integração com Engine Unity e Hand Tracking")
add_para(doc, "A integração com Unity 2022.3 LTS utiliza o Meta XR SDK (para Meta Quest 3) ou OpenXR (para portabilidade). Os parâmetros de 25 juntas são transmitidos via: (a) UDP socket local (mais rápido, para protótipo); ou (b) Unity ML-Agents / Barracuda (para inferência futura na engine). O avatar de mão utiliza o rig OVRHand ou XRHandSubsystem, mapeando diretamente as 25 juntas do skeleton. Testes de latência são realizados com instrumentação de loopback (timestamp no JSON → timestamp na renderização).")

add_title(doc, "4.7 Métricas de Avaliação")
add_para(doc, "Tabela 5 – Métricas de avaliação e instrumentos de mensuração")
add_para(doc, "Latência end-to-end: Tempo total JSON recebido → mão renderizada – Loopback de timestamps (NTP) – Meta: <150 ms (P95)")
add_para(doc, "Jitter: Desvio padrão da latência – Análise de série temporal – Meta: <5 ms")
add_para(doc, "Drift temporal: Diferença acumulada entre relógios – Cross-correlação – Meta: <10 ms/min")
add_para(doc, "Correlação JSON-movimento: Coeficiência de Pearson entre p_move e amplitude de movimento – Regressão linear – Meta: >0.8")
add_para(doc, "Acurácia de pose: Erro médio quadrático entre pose alvo e renderizada – Motion capture de referência – Meta: <5 cm / <15°")
add_para(doc, "Usabilidade: Percepção de facilidade de uso – SUS (System Usability Scale) – Meta: >68 pontos")
add_para(doc, "Presença: Senso de imersão – IPQ (Igroup Presence Questionnaire) – Meta: >4,0 (escala 1-7)")

add_title(doc, "4.8 Análise de Dados e Análise de Custo-Efetividade")
add_para(doc, "Análise estatística: descritiva, inferencial (teste t pareado para latência Unity vs. baseline; ANOVA para condições de movimento), correlação de Pearson entre métricas técnicas e scores de usabilidade. Software: Python (SciPy, StatsModels) e R (lme4, ggplot2).")
add_para(doc, "Análise de custo-efetividade: perspectiva SUS e saúde suplementar, horizonte 5 anos, comparadores: (a) camada open-source proposta; (b) desenvolvimento ad hoc; (c) solução comercial (ex: MindMaze, Hocoma). Custos: desenvolvimento, hardware, treinamento, manutenção. Desfechos: latência, usabilidade, potencial de escala. Análise de sensibilidade: ±20% (DRUMMOND et al., 2015).")

add_title(doc, "4.9 Desenho da Pesquisa e Passos Metodológicos")
add_para(doc, "Fase 1 – Especificação (Meses 1-6): Definição de schema JSON, protocolo de comunicação, arquitetura de módulos, revisão sistemática.")
add_para(doc, "Fase 2 – Implementação Core (Meses 4-10): Parser JSON, filtragem EMA, conversão cinemática, buffer temporal.")
add_para(doc, "Fase 3 – Integração Unity (Meses 8-14): Plugin C#, mapeamento de juntas, testes de latência em loopback.")
add_para(doc, "Fase 4 – Otimização (Meses 12-18): Redução de jitter, compensação de drift, predição de estado.")
add_para(doc, "Fase 5 – Validação (Meses 16-22): 15-20 participantes saudáveis, imagética motora, coleta de métricas técnicas e subjetivas.")
add_para(doc, "Fase 6 – Análise e Redação (Meses 20-24): Custo-efetividade, dissertação, artigo, defesa.")

page_break(doc)

# ============================================
# 5-9, REFERÊNCIAS, ANEXO, APÊNDICE
# ============================================
add_title(doc, "5 RESULTADOS ESPERADOS")
add_para(doc, "1. Camada de software funcional com documentação de API e protocolo JSON, licenciamento open-source (MIT).")
add_para(doc, "2. Demonstrador em Unity com Meta Quest 3, latência <150 ms e jitter <5 ms.")
add_para(doc, "3. Relatório técnico de sincronia temporal com benchmarks e recomendações.")
add_para(doc, "4. Relatório de análise de custo-efetividade com cenários SUS e suplementar.")
add_para(doc, "5. Artigo científico submetido a periódico Qualis A1-A2.")
add_para(doc, "6. Base tecnológica para ensaios clínicos futuros com pacientes pós-AVE no NERV.")

page_break(doc)

add_title(doc, "6 CRONOGRAMA")
add_para(doc, "Tabela 7 – Cronograma de execução do projeto")
add_para(doc, "Etapa | M1-3 | M4-6 | M7-9 | M10-12 | M13-15 | M16-18 | M19-21 | M22-24")
add_para(doc, "Especificação | XXX | X | | | | | |")
add_para(doc, "Implementação core | | | XXX | XXX | X | | |")
add_para(doc, "Integração Unity | | | | X | XXX | X | |")
add_para(doc, "Otimização | | | | | | XXX | XXX |")
add_para(doc, "Validação | | | | | | | XXX | XXX")
add_para(doc, "Análise/Redação | | | | | | | XXX | XXX")
add_para(doc, "Defesa | | | | | | | | XXX")

page_break(doc)

add_title(doc, "7 ORÇAMENTO E FINANCIAMENTO")
add_title(doc, "7.1 Orçamento")
add_para(doc, "Tabela 8 – Orçamento detalhado da pesquisa")
add_para(doc, "Equipamento EEG (OpenBCI Cyton) – Capital – R$ 3.500,00")
add_para(doc, "Headset VR (Meta Quest 3) – Capital – R$ 3.500,00")
add_para(doc, "Workstation GPU RTX 4060, 32GB – Capital – R$ 6.000,00")
add_para(doc, "Licenças software – Custeio – R$ 2.000,00")
add_para(doc, "Computação nuvem AWS/GCP – Custeio – R$ 3.000,00")
add_para(doc, "Materiais consumo – Custeio – R$ 1.500,00")
add_para(doc, "Congressos SBIS/IEEE EMBC – Custeio – R$ 4.000,00")
add_para(doc, "Publicação open access – Custeio – R$ 8.000,00")
add_para(doc, "Total – – R$ 31.500,00")
add_para(doc, "Os custos serão de responsabilidade do pesquisador, com complementação via editais CAPES/CNPq/FAPERGS. A camada open-source reduz 60-80% o custo de licenciamento vs. soluções proprietárias.")

page_break(doc)

add_title(doc, "8 CONSIDERAÇÕES ÉTICAS")
add_para(doc, "O presente estudo será submetido ao CEP da UFCSPA, conforme Resolução CNS 466/12 e Lei 11.794/08. A fase de validação com participantes saudáveis compreende: TCLE detalhado; riscos minimizados (desconforto leve de eletrodos, sessões VR ≤30 min); sigilo e anonimato de dados; benefícios para ciência; retirada voluntária. O projeto se enquadra nos termos da Resolução 466/12 do CONEP.")

page_break(doc)

add_title(doc, "9 CONSIDERAÇÕES SOBRE RISCOS")
add_para(doc, "Indisponibilidade de equipamento EEG – Média/Alto – Parcerias; simuladores de sinal")
add_para(doc, "Latência >150 ms – Média/Alto – Otimização pipeline; hardware dedicado; threads paralelas")
add_para(doc, "Baixa correlação JSON-movimento – Média/Alto – Ajuste de mapeamento; mais dados de calibração")
add_para(doc, "Jitter excessivo – Média/Médio – Buffer adaptativo; predição de estado; QoS de rede")
add_para(doc, "Ciberenjoo em participantes – Baixa/Médio – Sessões curtas; refresh ≥90 Hz; conforto visual")
add_para(doc, "Atraso aprovação CEP – Baixa/Médio – Submissão antecipada; diálogo contínuo")
add_para(doc, "Inviabilidade econômica SUS – Média/Médio – Análise de custo-efetividade; parcerias gestores")

page_break(doc)

# ============================================
# REFERÊNCIAS BIBLIOGRÁFICAS
# ============================================
add_title(doc, "REFERÊNCIAS BIBLIOGRÁFICAS")
add_para(doc, "")

referencias = [
    "ANG, K. K. et al. A randomized controlled trial of EEG-based motor imagery brain-computer interface robotic rehabilitation for stroke. Clinical EEG and Neuroscience, v. 46, n. 4, p. 310-320, 2015. Disponível em: https://pubmed.ncbi.nlm.nih.gov/25055897/. Acesso em: 18 jul. 2026.",
    "BAHIA, L. et al. Costs of stroke in Brazil: protocol for a societal cost-of-illness study. Value in Health Regional Issues, v. 22, p. 36-43, 2020. Disponível em: https://www.sciencedirect.com/science/article/pii/S2212109920300224. Acesso em: 18 jul. 2026.",
    "BLANKERTZ, B. et al. Optimizing spatial filters for robust EEG single-trial analysis. IEEE Signal Processing Magazine, v. 25, n. 1, p. 41-56, 2008. Disponível em: https://ieeexplore.ieee.org/document/4408441. Acesso em: 18 jul. 2026.",
    "BONINGER, M. L. et al. Technology and disability: findings from a National Institute on Disability and Rehabilitation Research conference. Journal of Rehabilitation Research & Development, v. 51, n. 6, p. 855-866, 2014. Disponível em: https://pubmed.ncbi.nlm.nih.gov/25356922/. Acesso em: 18 jul. 2026.",
    "CARAMIA, M. D. et al. Brain-computer interface for hand motor function rehabilitation in stroke: a systematic review and meta-analysis. Frontiers in Neuroscience, v. 15, p. 642732, 2021. Disponível em: https://www.frontiersin.org/articles/10.3389/fnins.2021.642732/full. Acesso em: 18 jul. 2026.",
    "DIETRICH, C. Neuroplasticity and motor recovery after stroke: evidence from functional neuroimaging. Restorative Neurology and Neuroscience, v. 39, n. 3, p. 185-196, 2021. Disponível em: https://pubmed.ncbi.nlm.nih.gov/33950291/. Acesso em: 18 jul. 2026.",
    "DRUMMOND, M. F. et al. Methods for the Economic Evaluation of Health Care Programmes. 4th ed. Oxford: Oxford University Press, 2015.",
    "FEIGIN, V. L. et al. Global, regional, and national burden of stroke and its risk factors, 1990–2019: a systematic analysis for the Global Burden of Disease Study 2019. The Lancet Neurology, v. 20, n. 10, p. 795-820, 2021. Disponível em: https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(21)00252-0/fulltext. Acesso em: 18 jul. 2026.",
    "FUGL-MEYER, A. R. et al. The post-stroke hemiplegic patient: a method for evaluation of physical performance. Scandinavian Journal of Rehabilitation Medicine, v. 7, n. 1, p. 13-31, 1975. Disponível em: https://pubmed.ncbi.nlm.nih.gov/1135616/. Acesso em: 18 jul. 2026.",
    "GBD 2019 STROKE COLLABORATORS. Global, regional, and national burden of stroke and its risk factors, 1990-2019: a systematic analysis for the Global Burden of Disease Study 2019. The Lancet Neurology, v. 20, n. 10, p. 795-820, 2021. Disponível em: https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(21)00252-0/fulltext. Acesso em: 18 jul. 2026.",
    "GORMAN, C. et al. A closed-loop AR-based BCI for real-world system control. In: IEEE Symposium Series on Computational Intelligence (SSCI). 2021. Disponível em: https://ieeexplore.ieee.org/xpl/conhome/9651419/proceeding. Acesso em: 18 jul. 2026.",
    "HAL. Designing functional prototypes combining BCI and AR. EuroXR Conference, 2023. Disponível em: https://hal.science/hal-03928273. Acesso em: 18 jul. 2026.",
    "HTC VIVE. OpenXR hand tracking SDK tutorial. VIVE Developer, 2024. Disponível em: https://developer.vive.com/resources/openxr/. Acesso em: 18 jul. 2026.",
    "KELLEY, R. E. et al. Functional recovery after stroke: a review of current therapeutic strategies. Current Neurology and Neuroscience Reports, v. 23, n. 5, p. 245-257, 2023. Disponível em: https://pubmed.ncbi.nlm.nih.gov/37192684/. Acesso em: 18 jul. 2026.",
    "KLEIM, J. A.; JONES, T. A. Principles of experience-dependent neural plasticity: implications for rehabilitation after brain damage. Journal of Speech, Language, and Hearing Research, v. 51, n. 1, p. S225-S239, 2008. Disponível em: https://pubmed.ncbi.nlm.nih.gov/18230848/. Acesso em: 18 jul. 2026.",
    "KWAKKEL, G. et al. Effects of augmented exercise therapy time after stroke: a meta-analysis. Stroke, v. 35, n. 11, p. 2529-2539, 2004. Disponível em: https://pubmed.ncbi.nlm.nih.gov/15472114/. Acesso em: 18 jul. 2026.",
    "LANG, C. E. et al. Upper extremity use in people with hemiparesis in the first six weeks after stroke. Journal of Neurologic Physical Therapy, v. 31, n. 2, p. 56-63, 2020. Disponível em: https://pubmed.ncbi.nlm.nih.gov/17534167/. Acesso em: 18 jul. 2026.",
    "LAWHERN, V. J. et al. EEGNet: a compact convolutional neural network for EEG-based brain-computer interfaces. Journal of Neural Engineering, v. 15, n. 5, p. 056013, 2018. Disponível em: https://iopscience.iop.org/article/10.1088/1741-2552/aace8c. Acesso em: 18 jul. 2026.",
    "LAWRENCE, E. S. et al. Estimates of the prevalence of acute stroke impairments and disability in a multiethnic population. Stroke, v. 32, n. 6, p. 1279-1284, 2001. Disponível em: https://pubmed.ncbi.nlm.nih.gov/11387487/. Acesso em: 18 jul. 2026.",
    "LECUYER, A. et al. Brain-computer interfaces, virtual reality, and videogames. IEEE Computer, v. 41, n. 10, p. 66-72, 2008. Disponível em: https://ieeexplore.ieee.org/document/4664317. Acesso em: 18 jul. 2026.",
    "LI, A. et al. Interactive and deep learning-powered EEG-BCI for wrist rehabilitation: a game-based prototype study. Neurobiology, v. 9, n. 3, p. 302, 2025. Disponível em: https://www.mdpi.com/journal/neurobiology. Acesso em: 18 jul. 2026.",
    "LO, A. C. et al. Robot-assisted therapy for long-term upper-limb impairment after stroke. New England Journal of Medicine, v. 362, n. 19, p. 1772-1783, 2010. Disponível em: https://pubmed.ncbi.nlm.nih.gov/20400552/. Acesso em: 18 jul. 2026.",
    "LOTTE, F. et al. Combining BCI with virtual reality: towards new applications and improved BCI. In: Towards Practical Brain-Computer Interfaces. Springer, 2012. p. 303-331. Disponível em: https://link.springer.com/chapter/10.1007/978-3-642-29746-5_14. Acesso em: 18 jul. 2026.",
    "MEHRHOLZ, J. et al. Electromechanical and robot-assisted arm training for improving activities of daily living, arm function, and arm muscle strength after stroke. Cochrane Database of Systematic Reviews, v. 2018, n. 9, 2018. Disponível em: https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD006876.pub5/full. Acesso em: 18 jul. 2026.",
    "META. Setup hand tracking in Unreal Engine. Meta Developers, 2026. Disponível em: https://developers.meta.com/horizon/documentation/unreal/unreal-hand-tracking/. Acesso em: 18 jul. 2026.",
    "MINISTÉRIO DA SAÚDE (BRASIL). Estratégias de atenção ao paciente com acidente vascular encefálico no SUS. Brasília: MS, 2023. Disponível em: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/a/acidente-vascular-cerebral-avc. Acesso em: 18 jul. 2026.",
    "MINISTÉRIO DA SAÚDE (BRASIL). Rede Nacional de Atenção Especializada (RENAME). Brasília: MS, 2022. Disponível em: https://www.gov.br/saude/pt-br/assuntos/atencao-especializada. Acesso em: 18 jul. 2026.",
    "MOVING: A multi-modal dataset of EEG signals and virtual glove hand tracking. Sensors, v. 24, n. 16, p. 5207, 2024. Disponível em: https://www.mdpi.com/1424-8220/24/16/5207. Acesso em: 18 jul. 2026.",
    "PFURTSCHELLER, G.; ARANIBAR, A. Evaluation of event-related desynchronization (ERD) preceding and following voluntary self-paced movement. Electroencephalography and Clinical Neurophysiology, v. 46, n. 2, p. 138-146, 1979. Disponível em: https://pubmed.ncbi.nlm.nih.gov/46855/. Acesso em: 18 jul. 2026.",
    "PFURTSCHELLER, G.; LOPES DA SILVA, F. H. Event-related EEG/MEG synchronization and desynchronization: basic principles. Clinical Neurophysiology, v. 110, n. 11, p. 1842-1857, 1999. Disponível em: https://pubmed.ncbi.nlm.nih.gov/10576479/. Acesso em: 18 jul. 2026.",
    "PISZCZ, A.; ROJEK, I.; MIKOŁAJEWSKI, D. Impact of virtual reality on brain-computer interface performance in IoT control: review of current state of knowledge. Applied Sciences, v. 14, n. 22, p. 10541, 2024. Disponível em: https://www.mdpi.com/2076-3417/14/22/10541. Acesso em: 18 jul. 2026.",
    "RIYAD, M.; KHALIL, M.; ADIB, A. MI-EEGNET: a novel convolutional neural network for motor imagery classification. Journal of Neuroscience Methods, v. 353, p. 109037, 2021. Disponível em: https://www.sciencedirect.com/science/article/pii/S0165027021000538. Acesso em: 18 jul. 2026.",
    "SALAMI, A. et al. EEG-ITNet: an explainable inception temporal convolutional network for motor imagery classification. IEEE Access, v. 10, p. 36672-36685, 2022. Disponível em: https://ieeexplore.ieee.org/document/9747584. Acesso em: 18 jul. 2026.",
    "SCHIRRMEISTER, R. T. et al. Deep learning with convolutional neural networks for EEG decoding and visualization. Human Brain Mapping, v. 38, n. 11, p. 5391-5420, 2017. Disponível em: https://onlinelibrary.wiley.com/doi/10.1002/hbm.23730. Acesso em: 18 jul. 2026.",
    "TAYLOR, R. M. et al. VRPN: a device-independent, network-transparent VR peripheral system. In: Proceedings of the ACM Symposium on Virtual Reality Software and Technology (VRST). 2001. p. 55-61. Disponível em: https://dl.acm.org/doi/10.1145/505008.505019. Acesso em: 18 jul. 2026.",
    "VOURVOPOULOS, A. et al. RehabNet: a distributed architecture for motor and cognitive neuro-rehabilitation. In: IEEE 15th International Conference on E-Health Networking, Applications & Services (Healthcom). 2013. p. 454-459. Disponível em: https://ieeexplore.ieee.org/document/6720703. Acesso em: 18 jul. 2026.",
    "VOURVOPOULOS, A.; BERMÚDEZ I BADIA, S. Motor priming in virtual reality for motor rehabilitation. In: International Conference on Virtual Rehabilitation (ICVR). 2015. Disponível em: https://ieeexplore.ieee.org/document/7458799. Acesso em: 18 jul. 2026.",
    "WOLPAW, J. R. et al. Brain-computer interfaces for communication and control. Clinical Neurophysiology, v. 113, n. 6, p. 767-791, 2002. Disponível em: https://pubmed.ncbi.nlm.nih.gov/12048038/. Acesso em: 18 jul. 2026.",
    "WOO, S. et al. An open source-based BCI application for virtual world tour and its usability evaluation. Frontiers in Human Neuroscience, v. 15, p. 675986, 2021. Disponível em: https://www.frontiersin.org/articles/10.3389/fnhum.2021.675986/full. Acesso em: 18 jul. 2026.",
    "ZEILER, S. R.; KRASCHI, K. R. The interaction between training and plasticity in the poststroke brain. Current Opinion in Neurology, v. 26, n. 6, p. 609-616, 2013. Disponível em: https://pubmed.ncbi.nlm.nih.gov/24136129/. Acesso em: 18 jul. 2026."
]

for ref in referencias:
    add_para(doc, ref, indent=Cm(0))

page_break(doc)

add_title(doc, "ANEXO")
add_para(doc, "")
add_para(doc, "Anexo A – Termo de Consentimento Livre e Esclarecido (TCLE)")
add_para(doc, "[O TCLE completo será incluído aqui, contemplando: identificação da pesquisa, objetivos, procedimentos, riscos e benefícios, garantias de sigilo, voluntariedade da participação, dados do pesquisador responsável e do CEP.]")

page_break(doc)

add_title(doc, "APÊNDICE")
add_para(doc, "")
add_para(doc, "Apêndice A – Glossário de Termos Técnicos")
add_para(doc, "BCI – Brain-Computer Interface (Interface Cérebro-Computador)")
add_para(doc, "CNN – Convolutional Neural Network (Rede Neural Convolucional)")
add_para(doc, "EEG – Electroencephalography (Eletroencefalografia)")
add_para(doc, "EMA – Exponential Moving Average (Média Móvel Exponencial)")
add_para(doc, "ERD/ERS – Event-Related Desynchronization/Synchronization")
add_para(doc, "JSON – JavaScript Object Notation (formato de intercâmbio de dados)")
add_para(doc, "LSL – Lab Streaming Layer (protocolo de streaming temporal)")
add_para(doc, "MI – Motor Imagery (Imagética Motora)")
add_para(doc, "Middleware – Camada de software intermediária entre aplicações")
add_para(doc, "VR – Virtual Reality (Realidade Virtual)")
add_para(doc, "ZeroMQ – Biblioteca de mensageria de alta performance")

add_para(doc, "")
add_para(doc, "Apêndice B – Especificação da API da Camada de Tradução")
add_para(doc, "[Documentação técnica detalhada: endpoints, schema JSON de entrada, formato de saída para Unity, exemplos de uso, parâmetros de configuração.]")

add_para(doc, "")
add_para(doc, "Apêndice C – Modelo de Análise de Custo-Efetividade")
add_para(doc, "[Planilha/template de análise de decisão em saúde com cenários de implantação no SUS e saúde suplementar.]")

# ============================================
# SALVAR DOCUMENTO
# ============================================
doc.save('Projeto_Qualificacao_Mestrado_Middleware_BCI_VR_AVE_FINAL.docx')
print("Documento salvo com sucesso!")