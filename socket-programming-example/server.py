import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT)) # Bind the server to the port and the server's IP address using a tuple

def handle_client(conn, addr):
    pass


def start():
    server.listen()

    # When a new connection occurs, server will accept the connection and
    while True:
        conn, addr = server.connect()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

print("[STARTING] Server is starting...")
print(f"[LISTENING] Server is listening on {SERVER}")
start()