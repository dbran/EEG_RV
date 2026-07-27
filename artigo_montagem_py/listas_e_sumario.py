
# ============================================
# LISTAS E SUMÁRIO
# ============================================

add_title(doc, "LISTA DE FIGURAS")
add_para(doc, "")

figuras = [
    "Figura 1 – Pirâmide argumentativa do projeto: do problema clínico à solução tecnológica",
    "Figura 2 – Arquitetura do sistema integrado NERV e posicionamento da camada de tradução",
    "Figura 3 – Schema da mensagem JSON de entrada e campos processados",
    "Figura 4 – Pipeline de dados: JSON → Python → Unity VR",
    "Figura 5 – Diagrama de classes do módulo de conversão cinemática",
    "Figura 6 – Mecanismos de sincronização temporal (buffer, interpolação, predição)",
    "Figura 7 – Interface de hand tracking no Unity (Meta XR SDK)",
    "Figura 8 – Diagrama de sequência da latência end-to-end (JSON recebido → mão renderizada)",
    "Figura 9 – Modelo de análise de custo-efetividade da camada open-source vs. soluções proprietárias"
]
for f in figuras:
    add_para(doc, f, indent=Cm(0))

page_break(doc)

add_title(doc, "LISTA DE TABELAS")
add_para(doc, "")

tabelas = [
    "Tabela 1 – Epidemiologia do AVE no Brasil: indicadores e fontes",
    "Tabela 2 – Comparação de abordagens de reabilitação motora pós-AVE",
    "Tabela 3 – Campos do schema JSON e mapeamento para parâmetros cinemáticos",
    "Tabela 4 – Especificações técnicas da engine Unity e API de hand tracking",
    "Tabela 5 – Métricas de avaliação e instrumentos de mensuração",
    "Tabela 6 – Análise de custo-efetividade: camada open-source vs. soluções comerciais",
    "Tabela 7 – Cronograma de execução do projeto",
    "Tabela 8 – Orçamento detalhado da pesquisa"
]
for t in tabelas:
    add_para(doc, t, indent=Cm(0))

page_break(doc)

add_title(doc, "LISTA DE QUADROS")
add_para(doc, "")

quadros = [
    "Quadro 1 – Requisitos funcionais e não-funcionais da camada de tradução",
    "Quadro 2 – Considerações éticas da pesquisa",
    "Quadro 3 – Análise de riscos e estratégias de mitigação"
]
for q in quadros:
    add_para(doc, q, indent=Cm(0))

page_break(doc)

add_title(doc, "LISTA DE GRÁFICOS")
add_para(doc, "")

graficos = [
    "Gráfico 1 – Incidência de AVE no Brasil por região (DATASUS, 2019-2023)",
    "Gráfico 2 – Benchmark de latência e jitter em sistemas BCI-VR da literatura",
    "Gráfico 3 – Projeção de custos por categoria orçamentária"
]
for g in graficos:
    add_para(doc, g, indent=Cm(0))

page_break(doc)

add_title(doc, "SUMÁRIO")
add_para(doc, "")

sumario = [
    "1 INTRODUÇÃO",
    "1.1 Contextualização e Justificativa para a Pesquisa",
    "1.1.1 O Acidente Vascular Encefálico como Problema de Saúde Pública no Brasil",
    "1.1.2 Limitações da Reabilitação Convencional e a Necessidade de Inovação Tecnológica",
    "1.1.3 A Integração BCI-VR como Solução e o Papel do Middleware",
    "1.1.4 O Grupo NERV e a Delimitação do Escopo deste Mestrado",
    "1.2 Questão de Pesquisa",
    "1.3 Objetivos",
    "1.3.1 Objetivo Geral",
    "1.3.2 Objetivos Específicos",
    "1.4 Contribuição Esperada para a Área",
    "1.5 Organização do Volume em Capítulos",
    "",
    "2 REFERENCIAL TEÓRICO",
    "2.1 Acidente Vascular Encefálico: Fisiopatologia, Sequelas e Reabilitação Neuromotora",
    "2.2 Interfaces Cérebro-Computador e Imagética Motora na Reabilitação pós-AVE",
    "2.3 Redes Neurais Convolucionais para Decodificação de Intenção Motora",
    "2.4 Realidade Virtual Imersiva em Neuroreabilitação",
    "2.5 Protocolos de Comunicação e Sincronização Temporal em Sistemas BCI-VR",
    "",
    "3 TRABALHOS RELACIONADOS",
    "3.1 Arquiteturas de Middleware para Integração BCI-VR",
    "3.2 Classificadores de EEG e Deep Learning (Contexto Tecnológico)",
    "3.3 Hand Tracking e Engines VR (Contexto Tecnológico)",
    "3.4 Síntese da Lacuna",
    "",
    "4 MATERIAIS E MÉTODOS",
    "4.1 Método de Pesquisa e Delineamento",
    "4.2 Arquitetura da Camada de Tradução e Sincronização",
    "4.3 Schema JSON e Protocolo de Comunicação",
    "4.4 Algoritmo de Conversão Probabilístico-Cinemática",
    "4.5 Mecanismos de Sincronização Temporal",
    "4.6 Integração com Engine Unity e Hand Tracking",
    "4.7 Métricas de Avaliação",
    "4.8 Análise de Dados e Análise de Custo-Efetividade",
    "4.9 Desenho da Pesquisa e Passos Metodológicos",
    "",
    "5 RESULTADOS ESPERADOS",
    "",
    "6 CRONOGRAMA",
    "",
    "7 ORÇAMENTO E FINANCIAMENTO",
    "",
    "8 CONSIDERAÇÕES ÉTICAS",
    "",
    "9 CONSIDERAÇÕES SOBRE RISCOS",
    "",
    "REFERÊNCIAS BIBLIOGRÁFICAS",
    "",
    "ANEXO",
    "",
    "APÊNDICE"
]

for item in sumario:
    add_para(doc, item, indent=Cm(0))

page_break(doc)
print("Listas e Sumário finalizados.")