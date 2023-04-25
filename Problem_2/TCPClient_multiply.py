from socket import *
serverName = '156.110.247.18'
serverPort = 80
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
request = "GET / HTTP/1.1\r\nHost: 156.110.247.18\r\n\r\n"
print("Send the request:")
print(request)
clientSocket.send(request.encode())
print("From the Server:");
response = clientSocket.recv(1024)
print(response.decode())
clientSocket.close()
