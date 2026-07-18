Inside EEg x VR no BRasil

Brazilian research in EEG-VR integration focuses on motor imagery for neurorehabilitation and supernumerary limb control. Studies utilize protocols like LSL for data synchronization, achieving improved motor outcomes through immersive digital twins and real-time feedback loops.

----

## Fundamentação Teórica

A integração entre Interfaces Cérebro-Computador (BCI) e Realidade Virtual (RV) baseia-se na premissa de que a imaginação motora (MI) ativa mecanismos neurais análogos à execução física de movimentos, facilitando a neuroplasticidade [1] [2] [3]. A literatura brasileira destaca o uso de avatares digitais ("gêmeos digitais") e cenários imersivos para reduzir o caráter abstrato das tarefas de MI [1] [2]. A incorporação de um "terceiro braço" virtual, ou membros supernumerários, explora ilusões de transferência corporal, onde a visualização de um avatar em primeira pessoa supera condições de treinamento convencionais (como o paradigma de Graz), embora possa induzir carga cognitiva adicional [1]. O objetivo central é transformar o treinamento passivo em controle ativo, construindo vias neurais *in vitro* que conectam o cérebro aos membros virtuais [4] [5].

----

## Trabalhos Relacionados

A pesquisa nacional e internacional, frequentemente citada em contextos de reabilitação e tecnologia assistiva, demonstra que a RV provê o feedback necessário para reforçar caminhos sensório-motores [6] [3] [7]. Estudos pioneiros no Brasil, como os experimentos de controle de cadeiras de rodas via EEG e RV, estabeleceram bases para o processamento de sinais e avaliação de interfaces [8]. Em paralelo, pesquisas globais enfatizam o uso de estímulos multissensoriais (visual, auditivo e tátil) para aumentar a densidade de potência espectral em bandas de alta frequência (gama) na área motora, acelerando a recuperação funcional [7]. A eficácia destas abordagens é validada por escalas clínicas (ex: Fugl-Meyer) e exames de imagem (fMRI), confirmando mudanças neuroplásticas significativas em pacientes crônicos pós-AVC [3] [5].

----

## Metodologia e Detalhes Técnicos

A implementação técnica de sistemas BCI-VR exige uma arquitetura robusta para comunicação de baixa latência e sincronização de dados. A integração é frequentemente realizada via protocolo *Lab Streaming Layer* (LSL), que permite o alinhamento temporal entre fluxos de EEG e eventos do ambiente virtual [5]. A modelagem 3D e a animação são tipicamente desenvolvidas em plataformas como Unity3D e 3ds Max, garantindo que a intenção motora capturada pelo EEG seja traduzida em movimento virtual imediato [4].

| Parâmetro | Detalhes de Implementação |
| :--- | :--- |
| **Comunicação** | Uso de LSL para sincronização de dados e *sockets* para troca de mensagens [5]. |
| **Classificação** | Algoritmos de Deep Learning e Redes Neurais Convolucionais (CNN) [9]. |
| **Feedback** | Visual (avatares), auditivo e háptico para aumentar a propriocepção [7]. |
| **Avaliação** | Precisão de classificação (MI), latência (ms) e escalas de carga (NASA-TLX) [1] [10] [9]. |

Os métodos de avaliação focam na precisão da classificação de MI (frequentemente > 60-67%) e na redução da latência do sistema, essencial para a imersão [1] [9]. A estabilidade do sistema é medida através da redução de erro espacial e da modulação de energia em bandas específicas (ex: banda beta, 15-20 Hz), que servem como evidência neurofisiológica da incorporação do membro virtual [10]. Em conformidade com os padrões de periódicos como *Research on Biomedical Engineering* (SBEM), a validação experimental exige relatórios rigorosos de carga de trabalho e segurança clínica para populações com comprometimentos motores severos [10] [5].

----

## Bibliografia

[1] J. A. R. Salas, “Do I have a third arm? Towards a Supernumerary Motor Imagery Brain-Computer Interface in Virtual Reality,” Jan. 2019, [Online]. Available: https://lume.ufrgs.br/handle/10183/194362

[2] K. Lakshminarayanan et al., “Motor Imagery Performance through Embodied Digital Twins in a Virtual Reality-Enabled Brain-Computer Interface Environment,” Journal of Visualized Experiments, May 2024, doi: 10.3791/66859.

[3] A. Vourvopoulos et al., “Efficacy and Brain Imaging Correlates of an Immersive Motor Imagery BCI-Driven VR System for Upper Limb Motor Rehabilitation: A Clinical Case Report,” Frontiers in Human Neuroscience, vol. 13, pp. 244–244, July 2019, doi: 10.3389/FNHUM.2019.00244.

[4] C. Pengcheng and G. Nuo, “Research of VR-BCI and Its Application in Hand Soft Rehabilitation System,” pp. 254–261, May 2021, doi: 10.1109/ICVR51878.2021.9483707.

[5] A. Vourvopoulos et al., “Effects of a Brain-Computer Interface With Virtual Reality (VR) Neurofeedback: A Pilot Study in Chronic Stroke Patients.,” Frontiers in Human Neuroscience, vol. 13, pp. 210–210, June 2019, doi: 10.3389/FNHUM.2019.00210.

[6] G. Saggio and C. A. Pinto, “Virtuality Supports Reality for e-Health Applications,” pp. 247–272, Jan. 2010, doi: 10.5772/13085.

[7] X. Shao et al., “[Virtual reality-brain computer interface hand function enhancement rehabilitation system incorporating multi-sensory stimulation].,” vol. 41, no. 4, pp. 656–663, Aug. 2024, doi: 10.7507/1001-5515.202312055.

[8] E. Souza, A. Cardoso, and E. Lamounier, “Experiment of controlling a wheelchair using virtual and augmented reality with brainwaves,” Jan. 2014.

[9] T. Karacsony, J. P. Hansen, H. K. Iversen, and S. Puthusserypady, “Brain Computer Interface for Neuro-rehabilitation With Deep Learning Classification and Virtual Reality Feedback,” p. 22, Mar. 2019, doi: 10.1145/3311823.3311864.

[10] J. Teng, S. Cho, and S. R. Lee, “Tri-manual interaction in hybrid BCI-VR systems: integrating gaze, EEG control for enhanced 3D object manipulation.,” vol. 19, pp. 1628968–1628968, Jan. 2025, doi: 10.3389/fnbot.2025.1628968.
