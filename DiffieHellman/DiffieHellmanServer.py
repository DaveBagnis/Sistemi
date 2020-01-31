import socket as sck

socketServer = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

socketServer.bind(("127.0.0.1",5050))

socketServer.listen(1)

conn, address = socketServer.accept()
print("Mi sono connesso ad Alice")

N = 9973
g = 1567
A = int(conn.recv(4096).decode())
print(f"Ho ricevuto da Alice il numero A = {A}")

b = int(input(f"Inserire numero 'b' compreso tra 1 e {N}: "))
B = ((g**b)%N)
conn.sendall(str(B).encode())
print(f"Ho inviato ad Alice il numero 'B'")

K = ((A**b)%N)
print(f"Il numero K è {K}")

conn.close()
socketServer.close()