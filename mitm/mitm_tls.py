import socket
import threading

LISTEN_HOST = '0.0.0.0'
LISTEN_PORT = 9998
SERVER_HOST = 'tls-server'
SERVER_PORT = 12346

def forward(source, destination, direction):
    while True:
        try:
            data = source.recv(4096)
            if not data:
                break
            print(f"[{direction}] {data.decode(errors='ignore')}")
            destination.sendall(data)
        except:
            break

    source.close()
    destination.close()

def start_mitm():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mitm_socket:
        mitm_socket.bind((LISTEN_HOST, LISTEN_PORT))
        mitm_socket.listen(1)
        print(f"[+] MITM in ascolto su {LISTEN_HOST}:{LISTEN_PORT}")

        while True:
            client_conn, client_addr = mitm_socket.accept()
            print(f"[+] Connessione intercettata da {client_addr}")

            server_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_conn.connect((SERVER_HOST, SERVER_PORT))

            threading.Thread(target=forward, args=(client_conn, server_conn, 'Client -> Server')).start()
            threading.Thread(target=forward, args=(server_conn, client_conn, 'Server -> Client')).start()

if __name__ == "__main__":
    start_mitm()