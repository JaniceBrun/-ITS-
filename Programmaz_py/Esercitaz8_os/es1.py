"""
Autore: Janice Brun
Data: 14/06/2026
Titolo: Scrivere una procedura che dato un percorso elenchi tutte le directories presenti.
"""
import os

def elenca_directories(percorso):
    for elemento in os.listdir(percorso):
        percorso_completo = os.path.join(percorso, elemento)
        if os.path.isdir(percorso_completo):
            print(percorso_completo)

elenca_directories("C:/Users/demet/Desktop")