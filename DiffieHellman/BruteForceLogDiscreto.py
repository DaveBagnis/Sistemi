N = 9973
g = 1567

A = int(input("Quanto vale A? "))
B = int(input("Quanto vale B? "))

for a in range(0,N):
    if ((g**a)%N) == A:
        print(f"Ho trovato a = {a}")

for b in range(0,N):
    if ((g**b)%N) == B:
        print(f"Ho trovato b = {b}")