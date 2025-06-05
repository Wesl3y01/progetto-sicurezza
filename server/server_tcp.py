import socket

def start_tcp_server(host='0.0.0.0', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"[+] Server TCP in ascolto su {host}:{port}...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"[+] Connessione accettata da {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"[>] Messaggio ricevuto: {data.decode()}")
                conn.sendall(b"ACK: " + data)

if __name__ == "__main__":
    start_tcp_server()