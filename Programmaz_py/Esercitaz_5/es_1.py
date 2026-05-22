"""
    Autore: Janice Brun
    Data: 15/05/2026
    Titolo: Progettare una funzione che accetti un numero indefinito di dizionari e restituisca un
    dizionario che è la concatenazione di tutti i dizionari indicati come parametro formale alla
    funzione. Scrivete uno script che utilizzi tale funzione.

    Esempio:
    diz1 = {'v1':1,'v2':2,'v3':3}
    diz2 = {'v4':4,'v5':5,'v6':6}
    diz3 = {'v7':7,'v8':8}

    Dizionario restituito: {'v1': 1, 'v2': 2, 'v3': 3, 'v4': 4,
    'v5': 5, 'v6': 6, 'v7': 7, 'v8': 8}
    
"""
# Creazione della funzione che accetta un numero indefinito di dizionari e restituisce un dizionario concatenato

def logica(*dizionari: dict) -> dict:
    """Funzione: funzione che accetta un numero indefinito di dizionari e restituisce un dizionario concatenato
    
    Parametri:
        *dizionari (dict): Un numero indefinito di dizionari da concatenare
    
    Restituisce:
        dict: Un dizionario che è la concatenazione di tutti i dizionari indicati come parametro formale alla funzione"""

    dizoutput_loc = {}
    prova = 0

    while prova == 0:
        for diz in dizionari:
            if not isinstance(diz, dict):
                prova += 1
                
            dizoutput_loc.update(diz)
        return dizoutput_loc
    else:
        print("Almeno uno dei parametri non è un dizionario")

# Funzione principale per eseguire il programma

def main():
    """Funzione: funzione principale per eseguire il programma
    
    Parametri: nessuno
    
    Restituisce: stampa il dizionario concatenato creato dai dizionari indicati come parametro formale alla funzione
    """
    dizoutput = {}
    
    # diz1 = []
    # diz2 = ('a', 'b', 'c')
    # diz3 = []
    diz1 = {'v1':1,'v2':2,'v3':3}
    diz2 = {'v4':4,'v5':5,'v6':6}
    diz3 = {'v7':7,'v8':8}
    
    dizoutput = logica(diz1, diz2, diz3)
    
    print(dizoutput)

if __name__ == '__main__':
    main()