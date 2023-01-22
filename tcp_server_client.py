import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5003)
print(sys.stderr, f'connecting to {server_address}')
sock.connect(server_address)

try:
	message = "This is the message. It will be repeated."
	print(sys.stderr, f'sending {message}')
	sock.sendall(message.encode())
	
	amount_received = 0
	amount_expected = len(message)
	
	while amount_received < amount_expected:
		data = sock.recv(16)
		amount_received += len(data)
		print(sys.stderr, f'received {data}')
finally:
	print(sys.stderr, 'closing socket')
	sock.close()

