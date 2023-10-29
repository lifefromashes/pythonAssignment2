import socket
import sys
import hashlib

print("Client Application")
print("Establish a connection to a server")
print("Available on the same host using PORT 5555")

PORT = 5555  # Port Number of Server

# Define a list of messages
messages = [
    "Message 1",
    "Message 2",
    "Message 3",
    "Message 4",
    "Message 5",
    "Message 6",
    "Message 7",
    "Message 8",
    "Message 9",
    "Message 10",
]

try:
    # Create a Socket
    clientSocket = socket.socket()

    # Get my local host address
    localHost = socket.gethostname()

    print("\nAttempt Connection to: ", localHost, PORT)

    clientSocket.connect((localHost, PORT))

    # Sending messages from the list to the server
    for i, msg in enumerate(messages):
        messageBytes = bytes(str(msg).encode("utf-8"))
        clientSocket.sendall(messageBytes)

        buffer = clientSocket.recv(2048)
        md5_hash = buffer.decode("utf-8")
        print(f"Received MD5 Hash for Message {i+1}: {md5_hash}")

except Exception as err:
    sys.exit(err)

finally:
    clientSocket.close()