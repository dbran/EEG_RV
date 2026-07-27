using UnityEngine.InputSystem;
using UnityEngine;
using TMPro;

public class BCIDebugController : MonoBehaviour
{
    public GameObject handProxy;
    public TMP_Text commandText;
    public TMP_Text connectionText;

    private string currentCommand = "no_move";
    private Vector3 startPos;

    void Start()
    {
        //teste de entrada
        Debug.Log("BCIDebugController iniciado");
        startPos = handProxy.transform.position;
        connectionText.text = "Modo teste local";
        ApplyCommand("no_move");
        Application.runInBackground = true;
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
        Debug.Log("ApplyCommand recebeu: " + command);
        currentCommand = command;
        commandText.text = "Comando atual: " + currentCommand;

        if (command == "left")
            handProxy.transform.position = startPos + new Vector3(-1.5f, 0f, 0f);
        else if (command == "right")
            handProxy.transform.position = startPos + new Vector3(1.5f, 0f, 0f);
        else
            handProxy.transform.position = startPos;
    }
}