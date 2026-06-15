"""
Autore: Janice Brun
Data: 14/06/2026
Titolo: Scrivere una procedura che dato un percorso elenchi tutte le directories presenti.
"""
# importo il modulo os per interagire con il sistema operativo

import os

# funzione che elenca le directories presenti in un percorso specificato

def elenca_directories(percorso: str):
    """funzione: elenca le directories presenti in un percorso specificato
    Args:
        percorso (str): percorso da cui partire per elencare le directories
    """
    for elemento in os.listdir(percorso):
        percorso_completo = os.path.join(percorso, elemento)
        if os.path.isdir(percorso_completo):
            print(percorso_completo)

# esempio path da cui partire per elencare le directories

elenca_directories("C:/Users/demet/Desktop")