import socket

ports = [21, 22, 23, 25, 80, 443, 445, 3306]

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)
    code = client.connect_ex("bancocn.com", port)
    if code == 0:
        print(port, "OPEN")