
from socket import *
# Create a TCP welcoming socket
welcomeSocket = socket(AF_INET, SOCK_STREAM)
# Bind it to the local IP and port 12345
serverIP = '127.0.0.1'
serverPort = 12345
serverAddress = (serverIP, serverPort)
welcomeSocket.bind(serverAddress)
# Welcome socket begins listening for incoming TCP requests
# Allows up to 1 pending requests for connection in the queue
welcomeSocket.listen(1)
print('The server is ready to receive')
while True:
    # server waits on accept() for incoming requests
    # a new connection socket is created on return
    connectionSocket, clientAddress = welcomeSocket.accept()
    clientIP, clientPort = clientAddress
    # receive a byte string from the connection socket
    messageBytes = connectionSocket.recv(1024)
    message = messageBytes.decode("utf-8")
    print(f'message from {clientIP}:{clientPort} = {message}')
    try:
        num_list = [int(num) for num in message.split(",")]
    except ValueError:
        # If message is not a list of integers, send "invalid input"
        connectionSocket.send("invalid input".encode("utf-8"))
        connectionSocket.close()
        continue

    # Calculate the product of the list and send it back
    product = 1
    for num in num_list:
        product *= num

    modifiedMessage = str(product)
    connectionSocket.send(modifiedMessage.encode("utf-8"))

    # close the connection socket to this client
    connectionSocket.close()
    # the welcoming socket is still open for new clients
