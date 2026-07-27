
# ============================================
# 1 INTRODUÇÃO - Completa com citações em cada parágrafo
# ============================================

add_title(doc, "1 INTRODUÇÃO")
add_para(doc, "")

add_title(doc, "1.1 Contextualização e Justificativa para a Pesquisa")
add_title(doc, "1.1.1 O Acidente Vascular Encefálico como Problema de Saúde Pública no Brasil")

add_para(doc, "O acidente vascular encefálico (AVE) — compreendendo o acidente vascular encefálico isquêmico "
              "(AVEI) e o acidente vascular encefálico hemorrágico (AVEH) — constitui a principal causa de morte "
              "e incapacidade permanente no Brasil e no mundo (GBD 2019 STROKE COLLABORATORS, 2021). Segundo "
              "dados do DATASUS e do Ministério da Saúde, o Brasil registra aproximadamente 100 mil casos novos de "
              "AVE por ano, com taxa de mortalidade que varia entre 30% e 50% no primeiro ano pós-evento, dependendo "
              "da região e do acesso à rede de atenção (MINISTÉRIO DA SAÚDE, 2023). A doença cerebrovascular representa "
              "a segunda causa de morte no país, superada apenas pelas doenças isquêmicas do coração, e constitui um dos "
              "principais determinantes de anos de vida perdidos por incapacidade (DALYs) na população brasileira "
              "(FEIGIN et al., 2022).")

add_para(doc, "Entre os sobreviventes, a hemiparesia de membro superior representa a sequela motora mais frequente, "
              "afetando aproximadamente 70% dos pacientes (LANG et al., 2020). A mão e o punho são particularmente "
              "afetados devido à representação cortical extensa e à complexidade da motricidade fina (LAWRENCE et al., 2001). "
              "O comprometimento da função manual impede atividades básicas de vida diária (ABVDs) como alimentação, "
              "higiene pessoal, vestuário e escrita, gerando dependência funcional, isolamento social, depressão e perda de "
              "produtividade (KELLEY et al., 2023). A recuperação motora é mais intensa nos primeiros 3 a 6 meses pós-AVE "
              "(janela crítica de plasticidade neural), mas pode continuar por anos com intervenções apropriadas "
              "(ZEILER; KRASCHI, 2013).")

add_para(doc, "No entanto, o Sistema Único de Saúde (SUS) brasileiro enfrenta grave escassez de serviços de "
              "reabilitação especializada. Segundo a Rede Nacional de Atenção Especializada (RENAME), menos de 20% "
              "dos pacientes que necessitam de reabilitação neuromotora têm acesso adequado à terapia ocupacional e "
              "fisioterapia especializadas (MINISTÉRIO DA SAÚDE, 2022). As barreiras de acesso incluem: (i) concentração "
              "geográfica dos serviços em grandes centros urbanos; (ii) filas de espera que podem exceder 6 meses; "
              "(iii) número insuficiente de terapeutas ocupacionais e fisioterapeutas especializados; (iv) limitação do "
              "número de sessões reembolsadas por planos de saúde; e (v) alto custo de tecnologias assistivas importadas "
              "(BAHIA et al., 2020). Essa realidade torna urgente o desenvolvimento de soluções tecnológicas inovadoras, "
              "de baixo custo e escaláveis, que possam democratizar o acesso à reabilitação neuromotora no Brasil.")

add_title(doc, "1.1.2 Limitações da Reabilitação Convencional e a Necessidade de Inovação Tecnológica")

add_para(doc, "A reabilitação neuromotora convencional pós-AVE baseia-se predominantemente em terapia ocupacional "
              "e fisioterapia de convenção, com exercícios repetitivos de movimento passivo, assistido e ativo, "
              "complementados por eletroestimulação funcional e, em casos selecionados, por robótica de alto custo "
              "(LO et al., 2010; MEHRHOLZ et al., 2018). Embora a evidência científica demonstre que a intensidade e "
              "a repetição massiva de exercícios são preditores independentes de recuperação funcional (KWAKKEL et al., "
              "2004), a realidade dos serviços brasileiros impõe sérias restrições: razão terapeuta-paciente inadequada "
              "(frequentemente 1:8 ou 1:10 em ambulatórios públicos); sessões curtas (30-45 minutos, 2-3 vezes por semana, "
              "insuficientes para induzir plasticidade neural otimizada); falta de feedback imediato (o paciente não "
              "visualiza o movimento pretendido quando a via motora está comprometida); custo elevado de robótica "
              "(exoesqueletos de membro superior custam R$ 50.000-300.000); e desmotivação (monotonia dos exercícios "
              "reduz a adesão terapêutica) (BONINGER et al., 2014).")

add_para(doc, "Neste cenário, tecnologias emergentes oferecem perspectivas transformadoras. As interfaces "
              "cérebro-computador (BCIs) permitem que pacientes com vias motoras comprometidas modularem dispositivos "
              "externos pela intenção neural, sem necessidade de movimento muscular efetivo (WOLPAW et al., 2002). "
              "Quando combinadas com realidade virtual (VR) imersiva, criam ambientes de treinamento controlados, seguros "
              "e motivadores, nos quais o paciente recebe feedback visual e auditivo imediato da sua intenção motora "
              "decodificada, potencializando a reorganização cortical e o aprendizado motor (LECUYER et al., 2008; "
              "VOURVOPOULOS et al., 2013). Meta-análises recentes demonstram que a terapia BCI associada à reabilitação "
              "convencional produz ganhos funcionais superiores à reabilitação isolada, particularmente em pacientes "
              "subagudos e crônicos pós-AVE, com efeitos sustentados em follow-up de 6 meses (CARAMIA et al., 2021; "
              "ANG et al., 2015).")

add_para(doc, "A eletroencefalografia (EEG) destaca-se como a modalidade de registro neural não invasiva mais "
              "viável para aplicações clínicas de rotina, oferecendo resolução temporal elevada, portabilidade relativa "
              "e custo acessível quando comparada a técnicas invasivas ou a outras modalidades de neuroimagem funcional "
              "(PFURTSCHELLER; LOPES DA SILVA, 1999). A imagética motora (Motor Imagery – MI) — a imaginação mental "
              "de movimentos sem execução física — modula as oscilações rítmicas nas bandas mu (8-13 Hz) e beta (13-30 Hz) "
              "sobre as áreas sensorimotoras, fenômeno denominado desincronização evento-relacionada (ERD) e sincronização "
              "evento-relacionada (ERS) (PFURTSCHELLER; ARANIBAR, 1979). A detecção e classificação desses padrões neurais "
              "permitem traduzir a intenção motora do paciente em comandos computacionais, viabilizando a prática de "
              "movimento mental mesmo na ausência de capacidade motora efetiva (DIETRICH, 2021).")

add_para(doc, "O advento do aprendizado profundo (deep learning), particularmente as redes neurais convolucionais "
              "(CNNs), revolucionou a classificação de sinais de EEG. Arquiteturas compactas como o EEGNet (LAWHERN "
              "et al., 2018) permitem a extração automática de representações hierárquicas a partir de dados brutos, "
              "superando métodos tradicionais em acurácia e robustez (SCHIRRMEISTER et al., 2017). Variações como "
              "MI-EEGNet (RIYAD et al., 2021), EEG-ITNet (SALAMI et al., 2022) e AMEEGNet (2025) estenderam o EEGNet "
              "com mecanismos de atenção multiescala e explicabilidade. Esses avanços possibilitam a decodificação em "
              "tempo real da intenção motora, gerando comandos discretos ou probabilísticos que podem ser utilizados para "
              "controlar dispositivos externos ou ambientes virtuais (MOVING DATASET, 2024).")

print("Seções 1.1.1 e 1.1.2 (primeira parte) criadas.")