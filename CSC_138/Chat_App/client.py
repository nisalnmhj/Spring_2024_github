#Group: Nishan Maharjan(nmaharjan@csus.edu), Seungji (seungjinchae@csus.edu)
#section : 03
import sys
import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode().strip()
            print(message)  # Display the received message to the user
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def main():
    if len(sys.argv) != 3:
        print("Usage : python3 client.py <server_hostname> <server_port>")
        return

    # Server details
    host = sys.argv[1]
    port = int(sys.argv[2])

    # Connect to server
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print("Connected to server.")
    except Exception as e:
        print(f"Error: {e}")
        return

    username = input("Enter JOIN with your username: ")

    # Send JOIN request
    try:
        client_socket.sendall(f"{username}".encode())
        response = client_socket.recv(1024).decode().strip()
        print(response)
    except Exception as e:
        print(f"Error: {e}")
        return

    # Start a separate thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Start sending requests
    while True:
        try:
            command = input("Enter command (LIST, MESG<username> <message>, BCST<message> , QUIT): ").strip().upper()
            client_socket.sendall(command.encode())
            if command == "QUIT":
                break
            elif command.startswith("MESG"):
                recipient, message = command.split(maxsplit=2)[1:]
                recipient = recipient.lower()
                client_socket.sendall(f"MESG {recipient} {message}".encode())
                response = client_socket.recv(1024).decode().strip()
                print(response)
                # No need to wait for response here, as the message will be received asynchronously
            elif command.startswith("BCST"):
                message = command[5:].strip()
                client_socket.sendall(f"BCST {message}".encode())
                response = client_socket.recv(1024).decode().strip()
                print(response)
            elif command == "LIST":
                response = client_socket.recv(1024).decode().strip()
                print(response)
            else:
                print("Invalid command")
        except Exception as e:
            print(f"Error: {e}")

    # Close connection
    client_socket.close()
    print("Disconnected from server.")

if __name__ == "__main__":
    main()
