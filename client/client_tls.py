import socket, ssl
import time

time.sleep(10)

HOST = 'tls-mitm'  # Passa attraverso il MITM
PORT = 9998    # Il MITM inoltra al server TLS su 12346

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE  # Solo per test

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname='tls-server') as ssock:
        print("[+] Connessione TLS stabilita con il server tramite MITM")
        messages = [
            "comunicazione riservata",
            "inviare credenziali",
            "numero carta: 1234-5678-9012-3456",
            "fine comunicazione"
        ]
        for msg in messages:
            ssock.sendall(msg.encode())
            time.sleep(1)
            data = ssock.recv(4096)
            print(f"[<] Risposta: {data.decode(errors='ignore')}")
