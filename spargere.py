import sys

comarg = sys.argv
lungarg = len(comarg)

if lungarg != 3:
    print("Format de intrare incorect!")
    print("Folositi: python proiect.py <fisier text de intrare - cu extensia .txt> <fisier binar de intrare - fara extensie>")
    exit()

inputf = comarg[1]
inputf2 = comarg[2]

f = open(inputf, "rb")
f2 = open(inputf2, "rb")

sirfin = ""

for i in range(14):
    byte = f.read(1)
    byte2 = f2.read(1)
    xbyte = ord(byte) ^ ord(byte2)
    sirfin += chr(xbyte)
print(sirfin)
f.close()
f2.close()