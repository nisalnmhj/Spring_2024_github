#Group: Nishan Maharjan(nmaharjan@csus.edu), Seungji (seungjinchae@csus.edu)
#section : 03
import socket
import threading
import sys


# Global variables
MAX_CLIENTS = 10
clients = {}  # Dictionary to store registered clients

def broadcast(message, sender=None):
    for username, conn in clients.items():
        if username != sender:
            try:
                conn.sendall(message.encode())
            except Exception as e:
                print(f"Error broadcasting message to {username}: {e}")

def user_left(username):
    message = f"{username} left the chat\n"
    broadcast(message)

def handle_client(conn, addr):
    """
    Function to handle each client connection in a separate thread.
    """
    username = None
    while True:
        try:
            data = conn.recv(1024).decode().strip()
            if not data:
                break

            # Parse client commands
            command = data.split()[0]
            if command == "JOIN":
                if len(clients) >= MAX_CLIENTS:
                    conn.sendall("Too Many Users\n".encode())
                else:
                    print("The Chat Server Started")
                    username = data.split(maxsplit=1)[1]
                    if username not in clients:
                        clients[username] = conn
                        print(f"{username} connected with {addr} ")
                        conn.sendall(f"{username} Joined\n".encode())
                        broadcast(f"{username} joined!\n", sender=username)
                    else:
                        conn.sendall("Username already taken\n".encode())
            elif command == "LIST":
                if username:
                    conn.sendall("\n".join(clients.keys()).encode())
                else:
                    conn.sendall("You are not registered\n".encode())
            elif command == "MESG":
                 if username:
                    data_parts = data.split(maxsplit=2)
                    if len(data_parts) >= 3:
                        recipient = data_parts[1].lower()
                        if recipient in clients:
                             message = data_parts[2]
                             clients[recipient].sendall(f"{username}: {message}\n".encode())
                             conn.sendall("Message sent\n".encode())
                        else:
                            conn.sendall("Unknown Recipient\n".encode())
                    else:
                        conn.sendall("Invalid MESG command format\n".encode())
                 else:
                    conn.sendall("You are not registered\n".encode())
            elif command == "BCST":
                if username:
                    message = data[5:].strip()
                    broadcast(f"{username}: {message}\n")
                    conn.sendall("Broadcast message sent\n".encode())
                else:
                    conn.sendall("You are not registered\n".encode())
            elif command == "QUIT":
                if username:
                    del clients[username]
                    user_left(username)
                break
            else:
                conn.sendall("Unknown Message\n".encode())
        except Exception as e:
            print(f"Error: {e}")
            break

    # Close connection
    conn.close()
    print(f"{username} left {addr}")


def main():
    # Server setup
    if len(sys.argv) != 2:
        print("Usage: python3 server.py <svr_port>")
        return

    try:
        port = int(sys.argv[1])
        if not 1024 <= port <= 65535:
            raise ValueError("Port number must be between 1024 and 65535")
    except ValueError as ve:
        print(f"Error: {ve}")
        return

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print("Server listening...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected with {addr}")

        # Start a new thread to handle the client
        threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == "__main__":
    main()
