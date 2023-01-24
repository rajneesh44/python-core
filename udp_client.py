import socket

 

msg_from_client       = "Hello UDP Server Hello UDP Server Hello UDP Server Hello UDP Server Hello UDP Server Hello UDP Server Hello UDP Server Hello UDP Server Hello UDP Server"
bytes_to_send         = str.encode(msg_from_client)
server_address_port   = ("127.0.0.1", 5001)
buffer_size          = 100

 
# Create a UDP socket at client side
udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
udp_client_socket.sendto(bytes_to_send, server_address_port)
msg_from_server = udp_client_socket.recvfrom(buffer_size)
msg = f"Message from Server {msg_from_server[0]}"

print(msg)