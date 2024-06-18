# server.py (to be run on your laptop)
import socket
import threading

clients = []

def handle_client(conn, addr):
    global clients
    print(f"Connection from {addr} has been established!")
    clients.append(conn)

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received from {addr}: {data.decode('utf-8')}")

            # Send a response back to the client
            response = "Acknowledged"
            conn.sendall(response.encode('utf-8'))
    except Exception as e:
        print(f"An error occurred with {addr}: {e}")
    finally:
        conn.close()
        clients.remove(conn)
        print(f"Connection from {addr} closed.")

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Allow multiple connections
    print("Server started, waiting for connections...")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    HOST = "0.0.0.0"  # Listen on all interfaces
    PORT = 65432      # Port to listen on

    start_server(HOST, PORT)
