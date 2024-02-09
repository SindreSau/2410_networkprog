import socket
import threading

HEADER = 64
PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname()) # Get the server's IP address
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT)) # Bind the server to the port and the server's IP address using a tuple

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # Receive the message length from the client
        if msg_length:
            msg_length = int(msg_length) # Convert the message length from string to integer
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(f"[{addr}] {msg}")
            if connected:
                conn.send("Message received".encode(FORMAT))
            else:
                conn.send("Disconnecting".encode(FORMAT))
    
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    # When a new connection occurs, server will accept the connection and
    while True:
        conn, addr = server.accept() # conn is the connection object, addr is the address of the client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") # -1 because the start() function is also a thread


if __name__ == "__main__":
    print("[STARTING] Server is starting...")
    start()