import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ("127.0.0.1", 8080)  # Address, IP and Port

sock.bind(addr)  # Socket, listen to this address

sock.listen()

# This function has a while loop and waiting for a connetion(result is a tuple)
result = sock.accept()
# Destructuring tuple same way as the 2 bootom ones (this is a client socket)
client, client_addr = result

#client = result[0]
#client_addr = result[1]

print("Got a connection from: ", client_addr)
client.send(b"Hello client")
# Netcat or nc allows you to connet to a socket(in terminal)
# A server is basically a socketcn
# 1 Run the program so the socket can start listeninig for connections (python3 file name)
# 2 Connect to it using netcat from another terminal because the program is still runnig on the first terminal (nc 127.0.0.1 8080)

# Server is the listenint socket
# Client is the connecting socket(browser)
