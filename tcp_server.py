import socket
import sys

#create a tcp/ip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to port
server_address = ('localhost', 5003)
print(sys.stderr, f'Startting up on {server_address} port')
sock.bind(server_address)



sock.listen(1)

while True:
	print(sys.stderr, 'waiting for a connection')
	connection, client_address = sock.accept()

	try: 
		print(sys.stderr, f'connection from {client_address}')
		while True:
			data = connection.recv(16)
			print(sys.stderr, f'recieved {data}')
			if data:
				print('sending data back to the client')
				connection.sendall(data)
			else:
				print(sys.stderr, f'no more data from {client_address}')
				break
	finally:
		connection.close()

		

