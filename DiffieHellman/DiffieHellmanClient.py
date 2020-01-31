import socket as sck

socketClient = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

socketClient.connect(("127.0.0.1",5050))
print("Mi sono connessa a Bruno")

N = 9973
g = 1567

a = int(input(f"Inserire numero 'a' compreso tra 1 e {N}: "))
A = ((g**a)%N)
socketClient.sendall(str(A).encode())
print("Ho inviato a Bruno il numero 'A'")

B = int(socketClient.recv(4096).decode())
print(f"Ho ricevuto da Bruno il numero B = {B}")
K = ((B**a)%N)
print(f"Il numero K è {K}")

socketClient.close()