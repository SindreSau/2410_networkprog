from socket import *
import argparse

# Parse the command line arguments
parser = argparse.ArgumentParser()
# IP address
parser.add_argument('-i', '--ip', help='IP address of the server', required=True)
# Port number
parser.add_argument('-p', '--port', help='Port number of the server', required=True)
# filename
parser.add_argument('-f', '--filename', help='Filename to request from the server')
# Parse the arguments
args = parser.parse_args()
if args.filename is None:
	args.filename = 'index.html'

# Print the arguments for debugging
print('IP address: ', args.ip)
print('Port number: ', args.port)
print('Filename: ', args.filename)

# Create a socket
client_socket = socket(AF_INET, SOCK_STREAM)

try:
	# Connect to the server
	client_socket.connect((args.ip, int(args.port)))

	# Send a GET request to the server with the filename
	client_socket.send(f'GET /{args.filename} HTTP/1.1\r\nHost: {args.ip}:{args.port}\r\n\r\n'.encode())

	# Create a buffer to store the response
	response = ''

	# Keep receiving data until there's no more to receive
	while True:
		data = client_socket.recv(1024)
		if not data:
			break
		response += data.decode()

	print(f'Response: {response}')

except Exception as e:
	print(f'Error: {e}')

finally:
	# Close the socket
	client_socket.close()