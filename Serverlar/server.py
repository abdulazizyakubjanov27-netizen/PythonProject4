import socket

HOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen()

print("Server ishlayapti...")

while True:
    conn, addr = server.accept()
    print("Ulandi:", addr)

    request = conn.recv(4096).decode()
    print("Request:\n", request)

    response = """HTTP/1.1 200 OK
Content-Type: text/html

<h1>Server ma'lumotni oldi</h1>
"""

    conn.sendall(response.encode())
    conn.close()