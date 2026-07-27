
# ============================================
# CAPA
# ============================================
for _ in range(6):
    add_center(doc, "")

add_center(doc, "UNIVERSIDADE FEDERAL DE CIÊNCIAS DA SAÚDE DE PORTO ALEGRE", bold=True)
add_center(doc, "")
add_center(doc, "Programa de Pós-Graduação em Tecnologias da Informação e Gestão em Saúde")

for _ in range(8):
    add_center(doc, "")

title = ("MIDDLEWARE PARA INTEGRAÇÃO DE DADOS DE ELETROENCEFALOGRAFIA "
         "E REDES NEURAIS CONVOLUCIONAIS EM ENGINES DE REALIDADE "
         "VIRTUAL PARA PROJEÇÃO DE MOVIMENTO DE MÃO: CONTRIBUIÇÃO "
         "AO SISTEMA INTEGRADO DE REABILITAÇÃO NEUROMOTORA "
         "PÓS-ACIDENTE VASCULAR ENCEFÁLICO")
add_center(doc, title, bold=True)

for _ in range(8):
    add_center(doc, "")

add_center(doc, "[NOME COMPLETO DO MESTRANDO]")

for _ in range(4):
    add_center(doc, "")

add_center(doc, "Orientador(a): Prof. Dr. / Profa. Dra. [Nome do Orientador]")
add_center(doc, "Coorientador(a): Prof. Dr. / Profa. Dra. [Nome do Coorientador, se houver]")

for _ in range(4):
    add_center(doc, "")

natureza = ("Projeto de Mestrado submetido ao Programa de Pós-Graduação em "
            "Tecnologias da Informação e Gestão em Saúde da Universidade Federal de "
            "Ciências da Saúde de Porto Alegre para qualificação.")
add_center(doc, natureza)
add_center(doc, "")
add_center(doc, "Área de Concentração: Tecnologias da Informação em Saúde")
add_center(doc, "Linha de Pesquisa: Informática em Saúde / Engenharia Biomédica Aplicada à Reabilitação")

for _ in range(6):
    add_center(doc, "")

add_center(doc, "Porto Alegre")
add_center(doc, "2026")

page_break(doc)
print("Capa finalizada.")