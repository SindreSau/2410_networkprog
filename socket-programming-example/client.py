import socket

HEADER = 64
PORT = 8080
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname()) # Get the server's IP address

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ==(bind on server, connect on client) ==
client.connect((SERVER, PORT)) # Connect the client to the server using a tuple

def send(msg):
    message = msg.encode(FORMAT) # Encode the message to bytes
    msg_length = len(message) # Get the length of the message
    send_length = str(msg_length).encode(FORMAT) # Encode the message length to bytes
    send_length += b" " * (HEADER - len(send_length)) # b" " is saying that we want to send a byte string with a space, and we want to send it HEADER - len(send_length) times
    client.send(send_length) # Send the message length
    client.send(message) # Send the message
    print(client.recv(2048).decode(FORMAT)) # Receive the message from the server 2048 because it's the buffer size


if __name__ == "__main__":
    send("Hello World!")
    send(DISCONNECT_MESSAGE) # Send the disconnect message so the server knows to disconnect the client