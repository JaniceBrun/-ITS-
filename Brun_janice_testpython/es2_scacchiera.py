"""Janice Brun

Scacchiera NxN
Input: nome studente
Intero: n
carattere ì: c

Output: scacchiera alternata con _.

"""
def scacchiera():

    nome = input('Inserisci il tuo nome: ')

    n = int(input("Inserisci la dimensione della scacchiera: "))

    c = input("inserisci il carattere da utilizzare: ")

    print(f"Scacchiera generata da: {nome}")

    for x in range(n):
        riga = ""
        for y in range(n * 2):
            if(x + y) % 2 == 0:
                riga += c
            else:
                riga += "_"
        print(riga)

if __name__ == '__main__':
    scacchiera()
