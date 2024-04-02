# import socket module
from socket import *
import threading

server_socket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
SERVER_PORT = 65432
server_socket.bind(('', SERVER_PORT))  # Bind the socket to localhost, port 65432
server_socket.listen(1)  # The '1' represents the number of clients that can wait for a connection


def handle_client(connection_socket):
	try:
		message = connection_socket.recv(1024).decode()
		filename = message.split()[1]
		if filename == '/':
			filename = '/index.html'
		f = open(filename[1:])
		output_data = f.read()
		connection_socket.send("HTTP/1.1 200 OK\r\n".encode())
		connection_socket.send("Content-Type: text/html\r\n\r\n".encode())
		for i in range(0, len(output_data)):
			connection_socket.send(output_data[i].encode())
		connection_socket.send("\r\n".encode())

	except IOError:
		connection_socket.send("HTTP/1.1 404 Not Found\r\n".encode())
		connection_socket.send("Content-Type: text/html\r\n\r\n".encode())
		error_file = open('404.html')
		output_data = error_file.read()
		for i in range(0, len(output_data)):
			connection_socket.send(output_data[i].encode())
		connection_socket.send("\r\n".encode())

	finally:
		connection_socket.close()


while True:
	print('Ready to serve...')
	connection_socket, addr = server_socket.accept()
	print('Connection from: ', addr)
	# Create a new thread for each client
	client_thread = threading.Thread(target=handle_client, args=(connection_socket,))
	client_thread.start()


# These lines will never be reached, but ill keep them here as they were a part of the skeleton code
server_socket.close()
sys.exit()  # Terminate the program after sending the corresponding data
