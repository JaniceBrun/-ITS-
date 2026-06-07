"""
Autore: Janice Brun
Data: 03/06/2026
Titolo: Scrivi una classe che legga un file di testo e stampi sul file: “output.txt” la parola più lunga
contenuta. [Facoltativo: stampi sul file: “output.txt” le prime N parole più lunghe, N è dato
in input dall'utente].
Istanziare la classe e provare i metodi implementati.

"""
# class Lettore con metodo lettura che legge un file di testo e restituisce il suo contenuto

class Lettore(object):
    """Classe che legge un file di testo e restituisce la parola più lunga contenuta al suo interno"""

    def __init__(self):
        pass

# metodo lettura che legge un file di testo e restituisce il suo contenuto

    def lettura(self):
        """Metodo che legge un file di testo e restituisce il suo contenuto"""
        with open("stringa.txt", "r") as fh:
            return fh.read()
    
# metodo maxword che prende in input il contenuto del file e restituisce la parola più lunga

    def maxword(self, contenutoFile: str):
        """Metodo che prende in input il contenuto del file e restituisce la parola più lunga
        
           Args: contenutoFile (str): Il contenuto del file di testo
           
           Returns: str: La parola più lunga contenuta nel file di testo"""
        
        parolaMax = max(contenutoFile.split(' '), key=len)

        return parolaMax
    
    # metodo scrittura che prende in input una parola e la scrive su un file di testo
    def scrittura(self, valore: str):
        """Metodo che prende in input una parola e la scrive su un file di testo

        Args: valore (str): La parola da scrivere su file
        """
        with open("outputes2.txt", "w") as fh:
            fh.write(valore)

# istanzio la classe e provo i metodi implementati

miao = Lettore()
miao.lettura()
miao.maxword(miao.lettura())
miao.scrittura(miao.maxword(miao.lettura()))