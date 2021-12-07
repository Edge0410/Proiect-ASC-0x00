# Encriptare / Decriptare

Fisierul folosit pentru encriptare/decriptare este *proiect.py*

### Modul de utilizare este urmatorul: 

python proiect.py <modul de criptare: encrypt/decrypt> <cheie secreta> <fisier text de intrare - cu extensia .txt> <fisier binar de iesire - fara extensie>

### Observatii:

- Fisierul de intrare trebuie sa aiba formatul .txt obligatoriu, spre exemplu input.txt / text.txt
- Fisierul de iesire trebuie sa NU aiba extensie
- Toti parametrii de mai sus ce se afla intre sageti < --- > sunt obligatorii
- Ambele operatii (encrypt/decrypt) se realizeaza cu acelasi fisier, doar se schimba primul parametru din linia de comanda, dupa caz
  
# Spargerea parolei
  
Spargerea parolei se realizeaza cu ajutorul fisierului *spargere.py*, care primeste ca parametrii fisierul input neecriptat si fisierul output encriptat, si realizeaza operatia XOR intre caracterele acestora, caracter cu caracter. Astfel, va fi afisata parola, aceasta repetandu-se de mai multe ori. In fisierul incarcat, se realizeaza XOR pentru primele 14 caractere deoarece am descoperit in prealabil, ruland cu o lungime mai mare, de exemplu 30, ca lungimea parolei echipei adverse este de 14 caractere, si astfel la rulare se afiseaza doar cheia de encriptare folosita.
