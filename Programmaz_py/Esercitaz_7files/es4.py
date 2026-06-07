"""
Autore: Janice Brun
Data: 03/06/2026
Titolo: Scrivere un programma che permetta di copiare il contenuto di un file in un altro file
"""
# Funzione che apre il file di input in modalità lettura e legge il suo contenuto

def leggi_file(input_file: str) -> str:
    """Funzione che apre il file di input in modalità lettura e legge il suo contenuto

    Args:
        input_file (str): Il nome del file di input

    Returns:
        str: Il contenuto del file di input
    """
    with open(input_file, "r") as fh:
        return fh.read()

def main():
    """Funzione che apre il file di input in modalità lettura e legge il suo contenuto, 
    poi apre un file di output in modalità scrittura e scrive il contenuto del file di input nel file di output"""
    
    with open("stringa.txt", "r") as inputFile:
        contenuto = inputFile.read()

    with open("es4output.txt", "w") as outputFile:
        outputFile.write(contenuto)

if __name__ == '__main__':
    main()