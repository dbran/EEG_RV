# Unity (step-by-step)

## Objetivo

Documentar a configuracao inicial do projeto Unity para receber comandos derivados do EEG/CNN e exibir uma primeira resposta visual na cena.

Nesta etapa, o objetivo nao e ainda animar uma mao 3D final. O objetivo e validar a cadeia:

```text
Python/CNN -> comando simplificado -> Unity -> resposta visual
```

## Documentos relacionados

- [contrato_dados_cnn_unity.md](file:///Users/denisemunchen/Documents/EEG_RV/documentos/EEG_VR/contrato_dados_cnn_unity.md)
- [BCIUDPReceiver.cs](file:///Users/denisemunchen/Documents/EEG_RV/documentos/EEG_VR/BCIUDPReceiver.cs)
- [bci_jsonl_to_unity_commands.py](file:///Users/denisemunchen/Documents/EEG_RV/python/bci_jsonl_to_unity_commands.py)
- [rodar_bci_bridge.sh](file:///Users/denisemunchen/Documents/EEG_RV/python/rodar_bci_bridge.sh)
- [bci_stream_example.jsonl](file:///Users/denisemunchen/Documents/EEG_RV/python/bci_stream_example.jsonl)

## Escopo atual

Este guia cobre:

1. criacao do projeto Unity;
2. configuracao basica da cena;
3. criacao de uma interface simples com `Canvas`;
4. uso de um `Cube` como proxy inicial da mao;
5. criacao e vinculacao do script `BCIDebugController.cs`;
6. uso do `Input System` atual da Unity para testes com teclado;
7. preparacao da recepcao via UDP para integrar Python e Unity;
8. substituicao do cubo por uma mao 3D (`Rigged Hand`) respondendo aos comandos.

Este guia ainda nao cobre:

1. leitura direta do `jsonl` dentro da Unity;
2. animacao final com rig, avatar ou blend tree;
3. definicao dos gestos finais da mao;
4. integracao final com cena de reabilitacao.

## 1. Criar o projeto Unity

No Unity Hub:

1. clicar em `New project`;
2. escolher o template `3D Core`;
3. definir o nome do projeto;
4. criar o projeto.

Recomendacao: usar um nome simples, por exemplo `EEG_RV_Unity`.

## 2. Conferir a cena inicial

Na cena inicial, garantir a existencia de:

- `Main Camera`
- `Directional Light`

Se a tela mostrar `Display 1 - No cameras rendering`, verificar:

1. se existe `Main Camera` na `Hierarchy`;
2. se a camera esta ativa;
3. se a camera esta apontando para a cena;
4. se `Target Display = Display 1`.

Configuracao minima sugerida:

- `Main Camera`
  - `Position`: `(0, 1, -6)`
  - `Rotation`: `(0, 0, 0)`
- `Directional Light`
  - manter padrao inicial

## 3. Criar os objetos basicos da cena

Criar os seguintes objetos:

1. `Plane`
2. `Cube`
3. `Canvas`
4. `Empty GameObject`

Renomear para:

- `Ground`
- `HandProxy`
- `Canvas`
- `BCIDebugController`

Configuracao minima sugerida:

- `Ground`
  - `Position`: `(0, -1, 0)`
- `HandProxy`
  - `Position`: `(0, 0, 0)`
  - `Scale`: `(1, 1, 1)`

## 4. Criar a interface no Canvas

Dentro do `Canvas`, adicionar 3 elementos de texto usando TextMeshPro:

1. `TitleText`
2. `CommandText`
3. `ConnectionText`

Criacao:

1. selecionar `Canvas`;
2. `UI -> Text - TextMeshPro`;
3. repetir 3 vezes;
4. renomear cada objeto.

Se a Unity solicitar recursos do TextMeshPro:

1. clicar em `Import TMP Essentials`.

Conteudo inicial sugerido:

- `TitleText`: `EEG -> Unity`
- `CommandText`: `Comando: no_move`
- `ConnectionText`: `Status: aguardando dados`

## 5. Configurar o novo Input System

Como o script foi ajustado para usar `UnityEngine.InputSystem`, verificar:

1. se o pacote `Input System` esta instalado;
2. se o projeto esta configurado para usar o novo sistema.

Checagem:

1. `Window -> Package Manager`
2. buscar `Input System`
3. instalar, se necessario

Depois:

1. `Edit -> Project Settings -> Player`
2. localizar `Active Input Handling`
3. escolher:
   - `Input System Package (New)`, ou
   - `Both`

Se a Unity pedir reinicio do editor, aceitar.

## 6. Criar o script `BCIDebugController.cs`

O script deve ficar na pasta `Assets` do projeto Unity.

Nome do arquivo:

```text
BCIDebugController.cs
```

O nome do arquivo deve ser igual ao nome da classe.

Versao de referencia usando `UnityEngine.InputSystem`:

```csharp
using UnityEngine;
using UnityEngine.InputSystem;
using TMPro;

public class BCIDebugController : MonoBehaviour
{
    public GameObject handProxy;
    public TMP_Text commandText;
    public TMP_Text connectionText;

    private Vector3 startPos;

    void Start()
    {
        Application.runInBackground = true;
        Debug.Log("BCIDebugController iniciado");
        startPos = handProxy.transform.position;
        connectionText.text = "Modo teste local";
        ApplyCommand("no_move");
    }

    void Update()
    {
        if (Keyboard.current != null && Keyboard.current.aKey.wasPressedThisFrame)
        {
            Debug.Log("Tecla A detectada");
            ApplyCommand("left");
        }

        if (Keyboard.current != null && Keyboard.current.dKey.wasPressedThisFrame)
        {
            Debug.Log("Tecla D detectada");
            ApplyCommand("right");
        }

        if (Keyboard.current != null && Keyboard.current.sKey.wasPressedThisFrame)
        {
            Debug.Log("Tecla S detectada");
            ApplyCommand("no_move");
        }
    }

    public void ApplyCommand(string command)
    {
        Debug.Log("Aplicando comando: " + command);
        commandText.text = "Comando: " + command;

        if (command == "left")
            handProxy.transform.position = startPos + new Vector3(-1.5f, 0f, 0f);
        else if (command == "right")
            handProxy.transform.position = startPos + new Vector3(1.5f, 0f, 0f);
        else
            handProxy.transform.position = startPos;
    }
}
```

## 7. Anexar o script ao objeto da cena

Este foi um ponto importante na configuracao.

Nao basta criar o arquivo `.cs`. O script precisa estar anexado a um `GameObject` da cena.

Passos:

1. selecionar o objeto vazio `BCIDebugController` na `Hierarchy`;
2. no `Inspector`, clicar em `Add Component`;
3. procurar `BCIDebugController`;
4. adicionar o script.

Se o script nao estiver anexado, ele nao executa `Start()` nem `Update()`.

## 8. Vincular as referencias no Inspector

Depois de anexar o script, preencher os campos publicos no `Inspector`:

- `Hand Proxy` -> arrastar o objeto `HandProxy`
- `Command Text` -> arrastar o objeto `CommandText`
- `Connection Text` -> arrastar o objeto `ConnectionText`

Sem essas referencias, o script nao sabe quais objetos controlar.

## 9. Testar a cena

Para testar:

1. salvar o script na IDE com `Cmd + S`;
2. voltar ao Unity;
3. esperar a recompilacao;
4. clicar em `Play`;
5. clicar na aba `Game` para garantir foco;
6. pressionar:
   - `A` -> `left`
   - `D` -> `right`
   - `S` -> `no_move`

Resultado esperado:

- o texto `CommandText` muda;
- o `HandProxy` se move;
- mensagens aparecem no `Console` do Unity.

Observacao:

- se o texto estiver quebrando em duas linhas, reduzir o texto exibido e/ou aumentar a largura do `Rect Transform` do `CommandText`.

## 10. Onde ver o `Debug.Log`

As mensagens de `Debug.Log` aparecem no `Console` da Unity, nao no console da IDE.

Abrir em:

1. `Window -> General -> Console`

Mensagens esperadas:

- `BCIDebugController iniciado`
- `Tecla A detectada`
- `Tecla D detectada`
- `Tecla S detectada`
- `Aplicando comando: left/right/no_move`

## 11. Problemas encontrados e como resolver

### 11.1. O objeto aparece, mas nao move

Verificar:

1. se o script esta anexado via `Add Component`;
2. se as referencias foram preenchidas no `Inspector`;
3. se a aba `Game` esta com foco;
4. se ha erro no `Console`.

### 11.2. `Display 1 - No cameras rendering`

Verificar:

1. se existe `Main Camera`;
2. se esta ativa;
3. se esta apontando para a cena.

### 11.3. `Debug.Log` nao aparece

Verificar:

1. se o script esta anexado;
2. se o nome do arquivo bate com o nome da classe;
3. se ha erro de compilacao;
4. se o filtro `Log` do `Console` esta habilitado.

### 11.4. Script criado, mas nao executa

Causa comum:

- o arquivo `.cs` existe em `Assets`, mas o componente nao foi adicionado ao objeto da cena.

## 12. Relacao com o projeto EEG -> CNN -> Unity

Nesta etapa, a Unity foi primeiro validada em modo local com teclado e depois preparada para receber comandos por UDP. Isso reduz o risco antes da substituicao do cubo por uma mao 3D.

Arquitetura validada localmente:

```text
Teclado -> BCIDebugController -> HandProxy
```

Arquitetura de integracao imediata:

```text
EEG -> CNN -> JSONL -> tradutor Python -> comando simplificado -> Unity
```

## 13. Testar a troca de teclado para UDP

Depois que a cena responder corretamente ao teclado, o proximo passo e substituir a entrada manual por dados vindos do Python.

Ordem sugerida:

1. manter a mesma cena;
2. manter o mesmo `HandProxy`;
3. trocar a origem do comando:
   - de teclado
   - para UDP vindo do script Python;
4. so depois substituir o cubo por uma mao 3D.

## 14. Criar o receptor UDP na Unity

Para este teste, a recomendacao e manter o `BCIDebugController` como responsavel pelo movimento e adicionar um segundo script apenas para receber os pacotes UDP.

Arquivo de referencia:

- [BCIUDPReceiver.cs](file:///Users/denisemunchen/Documents/EEG_RV/documentos/EEG_VR/BCIUDPReceiver.cs)

Passos:

1. copiar o arquivo `BCIUDPReceiver.cs` para a pasta `Assets` do projeto Unity;
2. voltar ao Unity e esperar a recompilacao;
3. selecionar o objeto vazio `BCIDebugController` na `Hierarchy`;
4. clicar em `Add Component`;
5. adicionar `BCIUDPReceiver`.

## 15. Vincular os campos do `BCIUDPReceiver`

No `Inspector`, preencher:

- `Controller` -> arrastar o proprio componente `BCIDebugController` do objeto atual;
- `Connection Text` -> arrastar o objeto `ConnectionText`;
- `Listen Port` -> manter `5005`.
- `Apply Interval Seconds` -> usar `0.35` para um teste visual mais claro.

Observacao:

- o `BCIDebugController` continua sendo o script que aplica `left`, `right` e `no_move`;
- o `BCIUDPReceiver` apenas recebe o pacote UDP e chama `ApplyCommand()`.
- para o teste no Editor da Unity funcionar sem depender de clique de foco, `Application.runInBackground = true` deve estar presente em `BCIDebugController` e em `BCIUDPReceiver`.

## 16. Comando Python para o teste UDP

No terminal do projeto EEG_RV, executar:

```bash
bash python/rodar_bci_bridge.sh --dedupe --sleep-ms 500 --udp-host 127.0.0.1 --udp-port 5005
```

Esse comando:

1. ativa o ambiente `eeg_rv`;
2. le o arquivo `python/bci_stream_example.jsonl`;
3. converte os eventos em comandos `no_move`, `left` e `right`;
4. espera `500 ms` entre os comandos para facilitar a visualizacao;
5. envia os comandos para a Unity por UDP.

## 17. Resultado esperado do teste

Com a Unity em `Play` e o comando Python rodando:

1. o texto `ConnectionText` deve mudar para algo como:
   - `Status: ouvindo UDP na porta 5005`
   - depois `UDP conectado | ultimo comando: left`
2. o `HandProxy` deve mudar de posicao de acordo com os comandos recebidos;
3. o `Console` da Unity deve exibir logs do tipo:
   - `BCIUDPReceiver ouvindo na porta 5005`
   - `Pacote UDP recebido: {...}`

Sequencia esperada com o arquivo de exemplo em modo `--dedupe`:

1. `no_move`
2. `left`
3. `no_move`
4. `right`

Observacao importante:

- se todos os pacotes chegarem praticamente ao mesmo tempo, o movimento pode parecer nao acontecer ou apenas o ultimo comando ficar visivel;
- por isso, esta versao usa uma fila no `BCIUDPReceiver` e tambem aceita um atraso opcional no script Python.

## 18.1. Observacao importante sobre foco da Unity

Durante os testes, foi observado o seguinte comportamento:

- o cubo so se movia depois que a interface da Unity recebia foco novamente;
- isso dava a impressao de que o UDP havia falhado, quando na verdade os pacotes estavam chegando normalmente.

Correcao aplicada:

1. adicionar `Application.runInBackground = true;` no `Start()` do `BCIDebugController`;
2. adicionar `Application.runInBackground = true;` no `Start()` do `BCIUDPReceiver`.

Conclusao pratica:

- para testes `Python -> UDP -> Unity` no Editor, esse ajuste e importante para que a aplicacao continue processando os comandos mesmo quando o foco sai temporariamente da janela da Unity.

## 18. Se o UDP nao funcionar

Verificar:

1. se a Unity esta em `Play`;
2. se o `BCIUDPReceiver` foi anexado ao objeto da cena;
3. se `Controller` aponta para o componente `BCIDebugController`;
4. se `Connection Text` aponta para `ConnectionText`;
5. se a porta `5005` esta igual na Unity e no Python;
6. se ha mensagens de erro no `Console` da Unity;
7. se o terminal Python esta realmente emitindo os pacotes.

Para confirmar a emissao no terminal, o script Python deve imprimir JSONs como:

```json
{"command": "no_move", "source_label": 0, "source_label_text": "SEM MOVIMENTO", "is_mi": false, "p_move": 0.17, "tau": 0.45, "group_id": 0, "timestamp": 0.0}
```

## 19. Proximo passo recomendado

Depois que a mao 3D responder ao UDP:

1. manter o mesmo contrato de dados;
2. substituir o deslocamento simples por animacao;
3. definir a hierarquia final entre `HandRoot`, `Rigged Hand` e o controlador;
4. evoluir da cena de teste para a cena de reabilitacao.

## 20. Estado atual consolidado

Itens ja realizados:

1. projeto Unity criado em `3D Core`;
2. cena basica com camera, luz, plano e cubo configurada;
3. `Canvas` com `TitleText`, `CommandText` e `ConnectionText` criado com `TextMeshPro`;
4. `BCIDebugController.cs` criado e anexado corretamente por `Add Component`;
5. referencias `HandProxy`, `CommandText` e `ConnectionText` vinculadas no `Inspector`;
6. uso do `UnityEngine.InputSystem` configurado e funcionando;
7. teste por teclado validado com os comandos `left`, `right` e `no_move`;
8. texto do comando encurtado para melhorar a legibilidade em uma linha;
9. `BCIUDPReceiver.cs` preparado para receber comandos vindos do Python;
10. script Python tradutor pronto para emitir os comandos por UDP;
11. recepcao UDP validada na Unity;
12. necessidade de `Application.runInBackground = true` identificada e aplicada nos dois scripts para evitar dependencia do clique na interface;
13. mao 3D importada na Unity;
14. mao 3D configurada para responder aos comandos no lugar do cubo de teste.

## 21. Substituicao do cubo por mao 3D

Nesta etapa, o asset `Rigged Hand` foi importado para a Unity e conectado ao mesmo fluxo de comando ja validado com o cubo.

Objetivo:

- manter o mesmo pipeline `Python -> UDP -> Unity`;
- trocar apenas o elemento visual de resposta.

Estrutura recomendada:

```text
BCIDebugController
HandRoot
  - Rigged Hand
Canvas
Ground
Main Camera
Directional Light
```

Regra pratica:

- `BCIDebugController` continua com a logica;
- `BCIUDPReceiver` continua recebendo os comandos;
- `HandRoot` ou o objeto visual equivalente passa a ser referenciado em `handProxy`;
- `Rigged Hand` fica como malha/asset visual controlado.

Resultado validado:

- a mao 3D ja responde aos comandos `left`, `right` e `no_move`;
- o cubo deixa de ser necessario como feedback principal;
- o prototipo passa a ter um feedback visual mais proximo do caso de uso do projeto.

Arquivos principais desta etapa:

- [Unity_step_by_step.md](file:///Users/denisemunchen/Documents/EEG_RV/documentos/EEG_VR/Unity_step_by_step.md)
- [contrato_dados_cnn_unity.md](file:///Users/denisemunchen/Documents/EEG_RV/documentos/EEG_VR/contrato_dados_cnn_unity.md)
- [BCIUDPReceiver.cs](file:///Users/denisemunchen/Documents/EEG_RV/documentos/EEG_VR/BCIUDPReceiver.cs)
- [bci_jsonl_to_unity_commands.py](file:///Users/denisemunchen/Documents/EEG_RV/python/bci_jsonl_to_unity_commands.py)
