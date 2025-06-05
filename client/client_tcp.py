import socket

messaggi = ["inizio comunicazione con il server", "questi messaggi sono molto importanti", "spero di non essere spiato", "ecco il mio indirizzo", "via dei matti n°9","ho finito"]

def start_tcp_client(host='mitm', port=9999):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"[+] Connesso al server TCP {host}:{port}")

        for msg in messaggi:
            client_socket.sendall(msg.encode())
            response = client_socket.recv(1024)
            print(f"[<] Risposta dal server: {response.decode()}")

if __name__ == "__main__":
    start_tcp_client()