"""
Autore: Janice brun
Data: 15/06/2026
Titolo: Scrivere un programma che esamini tutte le directories sotto un dato percorso e conti tutti
i files con una determinata estensione data in input. [In prima battuta fermatevi al primo
livello di profondità delle directories]"""

import os

#funzione per l'inserimento del path e dell'estensione

def inserimento():
    """
    Funzione per l'inserimento del path e dell'estensione
    
    Returns:
        percorso (str): Il percorso della directory da esaminare
        estensione (str): L'estensione dei file da contare
    """
    percorso = input("Inserire il path: ")
    estensione = input("Inserisci l'estensione: ")

    return percorso, estensione

# funzione per la ricerca dei file con una determinata estensione in una directory

def ricerca():
    """
    Funzione per la ricerca dei file con una determinata estensione in una directory
    
    arguments:
        percorso (str): Il percorso della directory da esaminare
        
        estensione (str): L'estensione dei file da contare
   
    """
    percorso, estensione = inserimento()

    if not estensione.startswith("."):
        estensione = "." + estensione

    contatore = 0 

    for elemento in os.listdir(percorso):
        percorso_completo = os.path.join(percorso, elemento)

        if os.path.isdir(percorso_completo):
            for file in os.listdir(percorso_completo):
                if file.endswith(estensione):
                    contatore += 1

    print(f"File {estensione} trovati: {contatore}")

if __name__ == "__main__":
    ricerca()