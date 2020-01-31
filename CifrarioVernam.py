numeri = range(0,26)
alfanum = {}
numalf = {}
parola_crittografata = []
chiave_crittografata = []

for k in numeri:
    x = chr(k+65)
    numalf[k] = x
    alfanum[x] = k

#utente inserisce chiave e parola
chiave = input("Inserisci la chiave: ")
chiave = chiave.upper()

phrase = input("Inserisci messaggio (MAX 26 caratteri): ")
phrase = phrase.upper()
if len(chiave)<len(phrase):
    print("Chiave troppo corta")
else:
    parolaChiara = []
    for i,c in enumerate(list(phrase)):
        x = (alfanum[c] - alfanum[chiave[i]] + 26) % 26
        parolaChiara.append(numalf[x])
    print(''.join(parolaChiara))
    phrase = input("Inserisci parola codificata:")
    parolaScura = []
    for i,c in enumerate(list(phrase)):
        x = (alfanum[c] + alfanum[chiave[i]] + 26) % 26
        parolaScura.append(numalf[x])
    print(''.join(parolaScura))

