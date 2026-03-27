import socket
import re

url = input("URL kiriting: ")

host = url.replace("http://", "").replace("https://", "").split("/")[0]

PORT = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, PORT))

request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

client.sendall(request.encode())

response = b""

while True:
    data = client.recv(4096)
    if not data:
        break
    response += data

client.close()

html = response.decode(errors="ignore")

links = re.findall(r'href="(.*?)"', html)

print("\nTopilgan linklar:\n")

for link in links:
    print(link)