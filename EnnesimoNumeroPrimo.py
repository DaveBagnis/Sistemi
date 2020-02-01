primiQuattro = [1,2,3,5]
def PosMagg6(posNPrimo):
    k = 6
    cntNPrimo = 4
    isPrime = True
    while True:
        for p in range(2, k//2):
            if (k % p == 0):
                isPrime = False

        if isPrime:
            cntNPrimo = cntNPrimo+1
            if (cntNPrimo == posNPrimo):
                break
        k = k+1
        isPrime = True
    
    print(f"Numero primo = {k}")

posNPrimo = int(input("Inserisci la posizione del numero primo: "))

if (posNPrimo > 4):
    PosMagg6(posNPrimo)
else:
    print(f"Numero primo = {primiQuattro[posNPrimo-1]}")