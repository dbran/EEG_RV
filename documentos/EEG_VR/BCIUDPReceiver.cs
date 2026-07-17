using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using TMPro;
using UnityEngine;

[Serializable]
public class BCICommandMessage
{
    public string command;
    public int source_label;
    public string source_label_text;
    public bool is_mi;
    public float p_move;
    public float tau;
    public int group_id;
    public float timestamp;
}

public class BCIUDPReceiver : MonoBehaviour
{
    public BCIDebugController controller;
    public TMP_Text connectionText;
    public int listenPort = 5005;

    private UdpClient udpClient;
    private Thread receiveThread;
    private volatile bool keepRunning;
    private readonly object syncRoot = new object();
    private readonly Queue<string> pendingCommands = new Queue<string>();
    private string latestStatus = "Status: aguardando dados UDP";
    public float applyIntervalSeconds = 0.35f;
    private float nextApplyTime;

    void Start()
    {
        Application.runInBackground = true;
        if (controller == null)
        {
            controller = GetComponent<BCIDebugController>();
        }

        StartUdpListener();
        SetConnectionText(latestStatus);
        
    }

    void Update()
    {
        string commandToApply = null;
        string statusToShow = null;

        lock (syncRoot)
        {
            if (pendingCommands.Count > 0 && Time.time >= nextApplyTime)
            {
                commandToApply = pendingCommands.Dequeue();
                nextApplyTime = Time.time + applyIntervalSeconds;
            }

            statusToShow = latestStatus;
        }

        SetConnectionText(statusToShow);

        if (!string.IsNullOrEmpty(commandToApply) && controller != null)
        {
            Debug.Log("UDP vai aplicar: " + commandToApply);
            controller.ApplyCommand(commandToApply);
        }
    }

    void OnDestroy()
    {
        StopUdpListener();
    }

    void OnApplicationQuit()
    {
        StopUdpListener();
    }

    private void StartUdpListener()
    {
        try
        {
            udpClient = new UdpClient(listenPort);
            keepRunning = true;
            receiveThread = new Thread(ReceiveLoop);
            receiveThread.IsBackground = true;
            receiveThread.Start();

            lock (syncRoot)
            {
                latestStatus = $"Status: ouvindo UDP na porta {listenPort}";
            }

            Debug.Log($"BCIUDPReceiver ouvindo na porta {listenPort}");
        }
        catch (Exception ex)
        {
            lock (syncRoot)
            {
                latestStatus = "Status: erro ao iniciar UDP";
            }

            Debug.LogError($"Erro ao iniciar UDP: {ex.Message}");
        }
    }

    private void ReceiveLoop()
    {
        IPEndPoint remoteEndPoint = new IPEndPoint(IPAddress.Any, 0);

        while (keepRunning)
        {
            try
            {
                byte[] payload = udpClient.Receive(ref remoteEndPoint);
                string json = Encoding.UTF8.GetString(payload);
                BCICommandMessage message = JsonUtility.FromJson<BCICommandMessage>(json);

                if (message == null || string.IsNullOrWhiteSpace(message.command))
                {
                    continue;
                }

                string normalizedCommand = message.command.Trim().ToLowerInvariant();

                lock (syncRoot)
                {
                    pendingCommands.Enqueue(normalizedCommand);
                    latestStatus = $"UDP conectado | ultimo comando: {normalizedCommand}";
                }

                Debug.Log($"Pacote UDP recebido: {json}");
            }
            catch (SocketException)
            {
                if (!keepRunning)
                {
                    break;
                }

                lock (syncRoot)
                {
                    latestStatus = "Status: erro de socket UDP";
                }
            }
            catch (Exception ex)
            {
                lock (syncRoot)
                {
                    latestStatus = "Status: erro ao ler pacote UDP";
                }

                Debug.LogError($"Erro ao processar pacote UDP: {ex.Message}");
            }
        }
    }

    private void StopUdpListener()
    {
        keepRunning = false;

        if (udpClient != null)
        {
            udpClient.Close();
            udpClient = null;
        }

        if (receiveThread != null && receiveThread.IsAlive)
        {
            receiveThread.Join(200);
            receiveThread = null;
        }
    }

    private void SetConnectionText(string value)
    {
        if (connectionText != null)
        {
            connectionText.text = value;
        }
    }
}
