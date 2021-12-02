import sys

comarg = sys.argv
lungarg = len(comarg)

if lungarg != 5:
    print("Format de intrare incorect!")
    print("Folositi: python proiect.py <modul de criptare: encrypt/decrypt> <cheie secreta> <fisier text de intrare - cu extensia .txt> <fisier binar de iesire - fara extensie>")
    exit()

cript = comarg[1]
parola = comarg[2]
inputf = comarg[3]
outputf = comarg[4]

def encrypt():
    f = open(inputf, "r")
    g = open(outputf, "wb")
    lung = len(parola)
    cont = 0
    sirfin = ""
    byte = f.read(1)
    while byte:
        xbyte = ord(byte) ^ ord(parola[cont % lung])
        sirfin += chr(xbyte)
        cont += 1
        byte = f.read(1)
    f.close()
    g.write(sirfin.encode('utf-8'))
    g.close()

def decrypt():
    f = open(inputf, "rb")
    g = open(outputf, "w")
    lung = len(parola)
    cont = 0
    sirfin = ""
    byte = f.read(1)
    while byte:
        xbyte = ord(byte) ^ ord(parola[cont % lung])
        sirfin += chr(xbyte)
        cont += 1
        byte = f.read(1)
    f.close()
    g.write(sirfin)
    g.close()

if cript == "encrypt":
    encrypt()
if cript == "decrypt":
    decrypt()











