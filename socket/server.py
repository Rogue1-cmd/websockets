import socket 
import threading

HEADER = 64
PORT = 5051
SERVER = "192.168.1.103" 
#SERVER = socket.gethostbyname(socket.gethostname()) #Get IP by name
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECTED"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    """
    Handles an individual client connection.

    This function is passed to a threading.Thread for each new connection to the server.
    It is responsible for receiving messages from the client and broadcasting them to all other connected clients.

    Parameters:
    conn - The socket object for the client's connection.
    addr - The address of the client.

    """
    print("[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE :
                connected = False

            print(f"[{addr}] {msg}")

    conn.close()

def start():
    """
    Starts the server.

    This function is called once to start the server and begin listening for connections.
    It is an infinite loop that waits for new connections and spawns threads to handle them.

    """
    server.listen()
    print(f"[LISTENING] @ {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    
print("Starting server at: ", PORT)
start()


