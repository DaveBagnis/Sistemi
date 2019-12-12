def MCD(a, b):
    while b>0:
        a, b = b, a%b       #assegno al numero più a sx il valore del numero più a dx, e al numero più a dx il modulo tra i due numeri (metodo di Euclide)
    return a

def mcm(a, b):
    return int(a * b / MCD(a, b))     #l'mcm di due numeri viene calcolato con il prodotto dei due numeri diviso il loro MCD

def chooseC(m):
    c = 2       #la prima condizione è che c debba essere compreso tra 1 e m (esclusi), quindi inizialmente lo imposto a 2 (primo numero > 1)
    while c < m:
        if (MCD(c, m) != 1):        #la seconda condizione è che l'MCD tra c e m sia uguale a 1, quindi se è diverso da 1 incremento c e riprovo
            c = c + 1
        else:
            return c        #se l'MCD è uguale a 1 ho trovato il mio c

def chooseD(c, m):
    d = 0       #la prima condizione è che c debba essere compreso tra 0 (incluso) e m (escluso), quindi inizialmente lo imposto a 0
    while d < m:
        if (((c * d) % m) != 1):        #la seconda condizione è che il prodotto tra c e d, se diviso con m, dia modulo = 1, quindi se è diverso da 1 incremento d e riprovo
            d = d + 1
        else:
            return d        #se l'MCD è uguale a 1 ho trovato il mio d

def algRSA():
    p = int(input("Inserisci numero p: "))
    q = int(input("Inserisci numero q: "))

    n = p * q       #numero n = prodotto tra p e q
    print(f"n = {n}")

    m = mcm(p-1, q-1)       #numero m = mcm tra p-1 e q-1
    print(f"m = {m}")

    c = chooseC(m)      #numero c tale che 1 < c < m e tale che MCD(c, m) = 1
    print(f"c = {c}")

    d = chooseD(c, m)       #numero d tale che o <= d < m e tale che (c*d) mod n = 1
    print(f"d = {d}")

    return d, c, n    

def encode(mex, c, n):
    return (mex ** c) % n       #dato un messaggio a da codificare, il messaggio criptato b sarà uguale ad a elevato alla c, il tutto mod n

def decode(mex, d, n):
    return (mex ** d) % n       #dato un messaggio b da decodificare, il messaggio decriptato a sarà uguale a b elevato alla d, il tutto mod n

d, c, n = algRSA()
mex = int(input("Inserire messaggio da codificare: "))
codMex = encode(mex, c, n)
print(f"Messaggio criptato: '{codMex}'")
decodMex = decode(mex, d, n)
print(f"Messaggio decriptato: '{decodMex}'")