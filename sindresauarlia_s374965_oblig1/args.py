import argparse

# Create the argument parser
parser = argparse.ArgumentParser()

# Define the optional arguments
parser.add_argument('-s', '--server', action='store_true', help='Enable the server mode')
parser.add_argument('-c', '--client', action='store_true', help='Enable the client mode')
parser.add_argument('-p', '--port', type=int, default=8088, help='Port address (default: 8088)')
parser.add_argument('-i', '--ip', type=str, default='10.0.0.2', help='IP address (default: 10.0.0.2)')

# Parse the arguments
args = parser.parse_args()

# Check if both server and client modes are enabled
if args.server and args.client:
    print('You cannot use both server and client modes at the same time')
    exit()

# Check if either server or client mode is enabled
if not args.server and not args.client:
    print('You should run either in server or client mode')
    exit()

# Check if the IP address is valid
ip_blocks = args.ip.split('.')
if len(ip_blocks) != 4 or not all(0 <= int(block) <= 255 for block in ip_blocks):
    print('Invalid IP. It must be in the format: 10.1.2.3')
    exit()

# Check if the port number is valid
if not 1024 <= args.port <= 65535:
    print('Invalid port. It must be within the range [1024, 65535]')
    exit()

# Display the corresponding IP and port addresses
if args.server:
    print(f'The server is running with IP address = {args.ip} and port address = {args.port}')
else:
    print(f'The client is running with IP address = {args.ip} and port address = {args.port}')