"""
Autore: Janice Brun
Data: 15/06/2026

Titolo: Scrivere un programma che elimini tutti i files che contengono nel nome una sequenza di
caratteri dati in input.
"""
#importo i moduli necessari

import os
import random 
import string

#funzione per generare nomi casuali di file

def genera_nomi_rndm(lunghezza=8):
    """Funzione per generare nomi casuali di file con estensione .py"""
    caratteri = (string.ascii_letters + string.digits).lower()
    nome = ''.join(random.choice(caratteri) for _ in range(lunghezza))
    
    return nome + ".py"

#funzione per creare una cartella di test con file da eliminare se non già presenti

def crea_dir_test():
    """funzione : creo cartella test con file da eliminare se non già presenti"""
    if not os.path.exists("test"):
        os.mkdir("test")
        print("dir creata")
    else:
        print("dir già presente")

    file_esistenti = len(os.listdir("test"))
    file_da_creare = 15 - file_esistenti    

    if file_da_creare <= 0:
        print("file già presenti")
        return

    for nomi in range(file_da_creare):
        file = genera_nomi_rndm()    
        percorso_file = os.path.join("test", file)


        with open(percorso_file, "w") as f:
            f.write("")
        print(f"file '{file} creato")

#funzione per eliminare i file che contengono una sequenza di caratteri nel nome

def eliminazione():
    """funzione per eliminare i file che contengono una sequenza di caratteri nel nome
    
        argomenti: sequenza di caratteri da cercare nel nome del file inseriti in input dall'utente"""

    crea_dir_test()

    percorso = os.path.join(os.path.dirname(__file__), "test")

    sequenza = input("Inserisci la sequenza da cercare: ")

    for file in os.listdir(percorso):
        percorso_completo = os.path.join(percorso, file)

        if os.path.isfile(percorso_completo):
            if sequenza in file:
                try:
                    os.remove(percorso_completo)
                    print("files eliminati")
                except Exception as err:
                    print("file non trovati")

    print("Fine elaborazioe")


if __name__ == "__main__":
    eliminazione()


