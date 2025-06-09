import socket, ssl, time

time.sleep(10)

HOST = '0.0.0.0'
PORT = 12346

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='certs/cert.pem', keyfile='certs/key.pem')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f"[+] Server TLS in ascolto su {HOST}:{PORT}...")

    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        print(f"[+] Connessione TLS accettata da {addr}")

        while True:
            data = conn.recv(4096)
            if not data:
                break
            print(f"[>] Ricevuto: {data.decode(errors='ignore')}")
            conn.sendall(b"SECURE ACK: " + data)
