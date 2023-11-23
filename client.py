import socket
import threading

HOST = '172.18.4.220'
PORT = 5000
BUFFER_SIZE = 4096

# create the client socket
client_socket = socket.socket(type=socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# ask the user for their name
name = input('Enter your name: ')
client_socket.send(name.encode())


def receive():
    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE).decode()
            print(message)
        except:
            # if an exception occurs, exit the loop
            client_socket.close()
            break


def send():
    while True:
        message = input()
        client_socket.send(message.encode())


# create two threads for sending and receiving messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
