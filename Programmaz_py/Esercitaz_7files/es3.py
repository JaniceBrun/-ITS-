"""
Autore: Janice Brun
Data: 03/06/2026
Titolo: Progetta una classe che legga un file di testo. Tale classe deve avere un metodo che
restituisca la parola con frequenza maggiore. [Suggerimento: si consideri l'esercizio che
contava le frequenze delle lettere in una stringa utilizzando i dictionary]
Provare il programma con testi classici come la Divina Commedia di Dante Alighieri
reperibile sul sito del progetto Gutenberg.

"""
# class LetturaFile che legge un file di testo e restituisce la parola con frequenza maggiore

class LetturaFile(object):
    """Classe che legge un file di testo e restituisce la parola con frequenza maggiore"""
   
    def __init__(self, nomefile: str):
        """Costruttore che legge il contenuto del file e lo memorizza in un attributo privato"""
          
        with open(nomefile, "r", encoding="utf-8") as dc:
            self.__testo = dc.read()

# getter e setter per l'attributo testo (privato)

    @property
    def testo(self):
        """ Metodo getter per l'attributo testo che restituisce il contenuto del file di testo letto"""
        return self.__testo
    
    @testo.setter
    def testo(self, testo):
        """ Metodo setter per l'attributo testo che verifica che il testo sia una stringa non vuota"""
        if not isinstance(testo, str):
            raise TypeError("Il testo deve essere formato stringa")
        if len(testo)== 0:
            raise ValueError("Il testo non può essere vuoto")
        self.__testo = testo
        
    # metodo parolaTop che restituisce la parola con frequenza maggiore nel testo, considerando solo parole con più di 3 lettere

    def parolaTop(self)-> str:
        """ Metodo che restituisce la parola con frequenza maggiore nel testo, considerando solo parole con più di 3 lettere"""
        parole = self.testo.lower().split()

        frequenza = {}
        for parola in parole:
            if len(parola) > 3:
                frequenza[parola] = frequenza.get(parola, 0) +1

        return max(frequenza, key=frequenza.get)
    
libro = LetturaFile("DC.txt")
print(libro.testo)
print(libro.parolaTop())

