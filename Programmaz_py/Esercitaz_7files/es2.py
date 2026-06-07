"""
Autore: Janice Brun
Data: 03/06/2026
Titolo: Scrivi una classe che legga un file di testo e stampi sul file: “output.txt” la parola più lunga
contenuta. [Facoltativo: stampi sul file: “output.txt” le prime N parole più lunghe, N è dato
in input dall'utente].
Istanziare la classe e provare i metodi implementati.

"""

class Lettore(object):

    def __init__(self):
        pass

    def lettura(self):
        with open("stringa.txt", "r") as fh:
            return fh.read()
    

    def maxword(self, contenutoFile):
        parolaMax = max(contenutoFile.split(' '), key=len)

        return parolaMax
    
    def scrittura(self, valore):
        
        with open("outputes2.txt", "w") as fh:
            fh.write(valore)

miao = Lettore()
miao.lettura()
miao.maxword(miao.lettura())
miao.scrittura(miao.maxword(miao.lettura()))