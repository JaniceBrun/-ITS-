"""
Autore: Janice Brun
Data: 03/06/2026
Titolo: Scrivere un programma che, leggendo da tastiera una stringa, la salvi su file “stringa.txt”.
Successivamente aprire il file “stringa.txt” e verificare il salvataggio.

"""
# Funzione per l'inserimento della stringa da tastiera, con controllo che non sia vuota

def inserimento():
    """Funzione per l'inserimento della stringa da tastiera, con controllo che non sia vuota"""

    stringa = input("Inserire una stringa: ")
    while len(stringa) == 0:
        stringa = input("La stringa non deve ssere vuota, inserire: ")
    return stringa

# Funzione principale del programma che gestisce l'inserimento della stringa, la scrittura su file e la verifica del salvataggio

def main():
    """Funzione principale del programma che gestisce l'inserimento della stringa, la scrittura su file e la verifica del salvataggio"""

    stringa = inserimento()
    with open("stringa.txt", "w") as fh:
        fh.write(stringa)
    print(stringa)

if __name__ == '__main__':
    main()
