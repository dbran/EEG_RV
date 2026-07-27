
# ============================================
# RESUMO
# ============================================
add_title(doc, "RESUMO")
add_para(doc, "")

add_para(doc, "Introdução: O acidente vascular encefálico (AVE) constitui a principal causa de morte e "
              "incapacidade permanente no Brasil, com aproximadamente 100 mil casos novos anualmente "
              "(MINISTÉRIO DA SAÚDE, 2023; GBD 2019 STROKE COLLABORATORS, 2021). Entre os sobreviventes, "
              "cerca de 70% apresentam hemiparesia de membro superior, comprometendo gravemente a autonomia "
              "funcional e a qualidade de vida (LANG et al., 2020; LAWRENCE et al., 2001). A reabilitação "
              "convencional, embora efetiva, enfrenta limitações de acesso, custo e intensidade terapêutica "
              "(LO et al., 2010; MEHRHOLZ et al., 2018). Tecnologias emergentes — interfaces cérebro-computador "
              "(BCI), realidade virtual (VR) imersiva e robótica — oferecem perspectivas de intervenção mais "
              "intensiva, personalizada e acessível (LECUYER et al., 2008; VOURVOPOULOS et al., 2013). "
              "No entanto, a interoperabilidade entre sistemas de aquisição de sinais neurais e engines de VR "
              "constitui um gargalo arquitetural que limita a escalabilidade clínica dessas soluções (LOTTE et al., 2012; "
              "HAL, 2023).")

add_para(doc, "Objetivo: Desenvolver e validar uma camada de software de tradução e sincronização temporal "
              "que receba mensagens JSON geradas por um classificador CNN/LM de eletroencefalografia (EEG), "
              "converta seus campos probabilísticos em parâmetros cinemáticos contínuos de articulação da mão, "
              "e os transmita à engine Unity para renderização sincronizada no headset de realidade virtual, "
              "permitindo a projeção precisa e de baixa latência do movimento de mão em ambientes imersivos de "
              "reabilitação neuromotora pós-acidente vascular encefálico.")

add_para(doc, "Métodos: Pesquisa aplicada de natureza tecnológica, com abordagem experimental. A camada de "
              "software será implementada em Python, arquitetada para receber mensagens JSON via protocolo de "
              "comunicação em tempo real (ZeroMQ/WebSocket), processar campos de classificação neural "
              "(label, p_combined, ema, p_move, threshold), converter probabilidades em parâmetros cinemáticos "
              "de 25 juntas da mão virtual, e transmiti-los à engine Unity com mecanismos de buffer circular, "
              "interpolação e compensação de latência. A validação compreenderá avaliação de latência end-to-end, "
              "jitter, sincronia temporal entre recepção do JSON e movimento renderizado, e usabilidade, com análise "
              "de viabilidade de implantação em cenários de saúde pública (SUS) e privada.")

add_para(doc, "Resultados Esperados: Camada de software funcional com documentação de API e protocolo de "
              "comunicação, demonstrador em engine Unity com headset VR, latência inferior a 150 ms e jitter "
              "controlado, análise de custo-efetividade comparativa e artigo científico submetido a periódico Qualis "
              "A1-A2 na área de Saúde ou Computação Aplicada.")

add_para(doc, "")
add_para(doc, "Palavras-chave: Acidente vascular encefálico; reabilitação neuromotora; interfaces cérebro-computador; "
              "eletroencefalografia; redes neurais convolucionais; realidade virtual; middleware; sincronia temporal; "
              "hemiparesia; tecnologias da informação em saúde.", indent=Cm(0))

page_break(doc)
print("Resumo finalizado.")