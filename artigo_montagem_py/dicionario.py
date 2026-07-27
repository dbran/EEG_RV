# ============================================
# APÊNDICE - DICIONÁRIO DE TERMOS
# ============================================
add_title(doc, "APÊNDICE - DICIONÁRIO DE TERMOS")
add_para(doc, "")

add_para(
    doc,
    "Jitter – Variação temporal na chegada, no processamento ou na renderização de mensagens "
    "ou eventos sucessivos em um sistema em tempo real. No contexto deste projeto, o jitter "
    "está associado à oscilação no intervalo entre o envio do comando pelo tradutor Python e "
    "a resposta visual observada na Unity. Valores elevados de jitter comprometem a percepção "
    "de continuidade do movimento e a sincronização entre inferência e feedback visual.",
    indent=Cm(0)
)

add_para(
    doc,
    "Latência – Intervalo de tempo transcorrido entre a geração de uma informação em um módulo "
    "do sistema e sua efetiva manifestação em outro módulo. Nesta pesquisa, refere-se "
    "principalmente ao tempo entre a saída da classificação EEG, o envio do comando pela camada "
    "intermediária em Python e a atualização da mão virtual na Unity. A latência é uma métrica "
    "central para avaliar a viabilidade do protótipo em aplicações de reabilitação em tempo real.",
    indent=Cm(0)
)

add_para(
    doc,
    "Inoperabilidade – Condição em que um sistema, componente ou serviço deixa de executar sua "
    "função esperada de forma total ou parcial. No escopo deste protótipo, a inoperabilidade pode "
    "estar relacionada a falhas de comunicação entre processos, perda de pacotes, erros de "
    "sincronização ou indisponibilidade de módulos da cadeia EEG -> Python -> Unity -> mão virtual.",
    indent=Cm(0)
)

add_para(
    doc,
    "Imagética motora – Processo cognitivo no qual o indivíduo imagina a execução de um "
    "movimento sem realizá-lo fisicamente. Em sistemas BCI baseados em EEG, a imagética motora "
    "é utilizada para provocar padrões neurofisiológicos detectáveis e classificáveis, permitindo "
    "converter a intenção de movimento em comandos de controle para aplicações como a mão virtual "
    "em realidade virtual.",
    indent=Cm(0)
)

add_para(
    doc,
    "Ad hoc – Expressão usada para designar soluções provisórias, pontuais ou construídas para "
    "atender a uma necessidade específica imediata, sem necessariamente seguir uma arquitetura "
    "mais geral, modular ou escalável. No contexto de software, soluções ad hoc costumam resolver "
    "um problema local de forma rápida, porém podem dificultar manutenção, reutilização e "
    "evolução do sistema em etapas posteriores.",
    indent=Cm(0)
)

page_break(doc)
print("Dicionário finalizado.")
