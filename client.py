import socket  # Import the socket module

host = 'localhost'  # Define the host
port = 8895 # Define the port

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
sock.connect((host,port))

# Send the file name to the server
fileName = 'abc.txt'
sock.send(fileName.encode())

# Receive and print the contents of the file from the server
readFile = sock.recv(1024)
print(readFile.decode())

# Close the socket connection
sock.close()
