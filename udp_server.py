import socket

local_ip = 'localhost'
local_port = 5001
buffer_size = 100

msgFromServer = "Hello UDP Client"
bytes_to_send = str.encode(msgFromServer)

#create a datagram socket
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#Bind to address and ip
udp_socket.bind((local_ip, local_port))

print(f"UDP server up and listening at {local_ip}:{local_port}")

#listen for incoming datagrams
while True:
    bytes_address_pair = udp_socket.recvfrom(buffer_size)
    message = bytes_address_pair[0]
    address = bytes_address_pair[1]
    
    print(f"Message from Client: {message}")
    print(f"Client ip address: {address}")

    #sending a reply to client
    udp_socket.sendto(bytes_to_send, address)