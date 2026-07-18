# Setup LSL no Projeto

## Ambiente oficial

Este projeto esta padronizado para usar **somente** o ambiente `conda` chamado `eeg_rv`.

Nao use `.venv` e `conda` ao mesmo tempo. Se o prompt aparecer como:

```bash
(eeg_rv) (.venv)
```

saia do `.venv` antes de rodar qualquer script:

```bash
deactivate
conda activate eeg_rv
```

O Python esperado para este projeto e:

```bash
/Users/denisemunchen/anaconda3/envs/eeg_rv/bin/python
```

## Estrutura criada

- `external/labstreaminglayer`: clone do repositório oficial do LSL com submódulos.
- `python/test_lsl_sender.py`: script simples para testar envio de stream LSL em Python.

## Repositório oficial clonado

- `https://github.com/sccn/labstreaminglayer`

O clone foi feito com submódulos para trazer `liblsl`, bindings Python e integração Unity:

```bash
git clone --recurse-submodules https://github.com/sccn/labstreaminglayer.git
```

## Ambiente Python

O ambiente configurado é:

```bash
conda activate eeg_rv
```

Ou, para recriar o ambiente a partir do projeto:

```bash
conda env create -f environment.yml
conda activate eeg_rv
```

Se o terminal ainda nao reconhecer `conda`, rode antes:

```bash
source ~/.zshrc
```

Para conferir se voce esta no ambiente certo:

```bash
python -c "import sys; print(sys.executable)"
python -c "import pylsl; print(pylsl.__file__)"
```

## Bibliotecas instaladas

- `pylsl`
- `numpy`
- `scipy`
- `pandas`
- `matplotlib`

## Teste rapido

Ative o ambiente:

```bash
conda activate eeg_rv
```

Inicie um stream LSL de teste:

```bash
python python/test_lsl_sender.py
```

Ou use o script de conveniencia:

```bash
bash python/rodar_lsl_sender.sh
```

## Uso com Unity

Para Unity, a base relevante ja esta no clone:

- `external/labstreaminglayer/LSL/liblsl-Unity`

Essa parte deve ser importada no projeto Unity quando voce for integrar a cena/VR.

## Observacao

Durante a instalacao, o sandbox do ambiente bloqueou a escrita no historico interno do `conda`, mas o ambiente e os testes de `pylsl` funcionaram normalmente neste projeto.
