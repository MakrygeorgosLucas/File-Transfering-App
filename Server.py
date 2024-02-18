import socket  # Import the socket module

host = 'localhost'  # Define the host
port = 9090  # Define the port

# Create a TCP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
sock.bind((host,port))

# Listen for incoming connections
sock.listen(1)

# Print a message indicating the server is running and listening for client requests
print("The server is running and is listening to clients requests")

# Accept incoming connection
conn , adress = sock.accept()

try:
    # Receive the file name from the client
    fileName = conn.recv(1024)
    
    # Open the file in binary mode for reading
    file = open(fileName , 'rb')
    
    # Read the contents of the file
    readFile = file.read()
    
    # Send the contents of the file to the client
    conn.send(readFile)

    # Close the file
    file.close()

except FileNotFoundError:
    # If the file is not found, send an error message to the client
    conn.send("File not found on the server".encode())

# Close the connection
conn.close()
