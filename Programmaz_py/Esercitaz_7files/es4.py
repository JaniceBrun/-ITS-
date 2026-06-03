"""
Autore: Janice Brun
Data: 03/06/2026
Titolo: Scrivere un programma che permetta di copiare il contenuto di un file in un altro file
"""

def main():
    with open("stringa.txt", "r") as inputFile:
        contenuto = inputFile.read()

    with open("es4output.txt", "w") as outputFile:
        outputFile.write(contenuto)

if __name__ == '__main__':
    main()