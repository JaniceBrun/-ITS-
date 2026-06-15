"""
Autore: Janice brun
Data: 15/06/2026
Titolo: Scrivere un programma Python per eseguire un comando del sistema operativo usando il
modulo os."""

import os

# funzioni per eseguire il comando del sistema operativo e filtrare i file con estensione .py

def ottieni_comando(percorso=None):
    """Restituisce il comando giusto per il sistema operativo"""
    cmd ="dir" if os.name == 'nt' else 'ls'
    if percorso:
        cmd += f" {percorso}"
    return cmd


def esegui_comando(comando):
    """
    Esegue il comando e restituisce l'output
    
    argomento: comando (str): il comando da eseguire
    
    ritorna: str: l'output del comando
    """
    risultato = os.popen(comando)
    contenuto = risultato.read()
    return contenuto

def filtra_file(contenuto: str, estensione: str):
    """
    funzione: Filtra le righe in base all'estensione
    
    argomento: contenuto (str): l'output del comando
               estensione (str): l'estensione da filtrare
               
    ritorna: list: le righe filtrate
    """
    righe = contenuto.split("\n")

    risultati = []
    for riga in righe:
        if estensione in riga:
            risultati.append(riga)

    return risultati

def main():
    """Funzione: Esegue il programma principale
    """
    percorso = input("Inserisci il percorso o Enter per cartella corrente): ")

    comando = ottieni_comando(percorso if percorso else None)
    contenuto = esegui_comando(comando)
    files = filtra_file(contenuto, ".py")

    for file in files:
        if file.strip():
            print(file)

if __name__ == "__main__":
    main()

