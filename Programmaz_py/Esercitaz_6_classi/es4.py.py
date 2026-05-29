"""
    Autore: Janice Brun
    Data: 29/05/2026
    Titolo: Si definisca una classe Persona che abbia i seguenti attributi:
    ● nome
    ● indirizzo
    ● età
    Tale classe contiene i seguenti metodi: il costruttore, l'overriding del metodo __str__ e tutti i
    metodi getter e setter degli attributi.
    Si vogliono derivare dalla classe Persona le seguenti classi:
    ● Studente
    ● Lavoratore
    La prima deve avere gli attributi aggiuntivi:
    ● Scuola
    ● Media voti
    La seconda deve avere gli attributi aggiuntivi:
    ● Azienda
    ● Stipendio
    Aggiungere tutti i metodi getter e setter relativi agli attributi aggiuntivi.
    Inoltre effettuare l'overriding dei costruttori e del metodo str inserendo gli attributi
    aggiuntivi.
    Provare le tre classi instanziando almeno un oggetto per classe e provando qualche
    metodo.
"""

class Persona(object):
    def __init__(self, nome, indirizzo, eta):
        self.__nome = nome
        self.__indirizzo = indirizzo
        self.__eta = eta

    @property
    def nome(self):
        """Metodo getter per l'attributo nome"""
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        """Metodo setter per l'attributo nome che verifica che il valore sia una stringa non vuota"""
        if isinstance(nome, str) and len(nome) > 0:
            self.__nome = nome
        else:
            raise ValueError("Invalid name")
        
    # getter e setter per indirizzo

    @property
    def indirizzo(self):
        return self.__indirizzo
    
    @indirizzo.setter
    def indirizzo(self, indirizzo):
        self.__indirizzo = indirizzo


    # getter e setter per età
        
    @property    
    def eta(self):
        """Metodo getter per l'attributo eta"""
        return self.__eta
    
    @eta.setter
    def eta(self, eta):
        """Metodo setter per l'attributo eta che verifica che il valore sia un numero intero positivo"""
        if isinstance(eta, int) and eta > 0:
            self.__eta = eta
        else:
            raise ValueError("Invalid age")
        
    def __str__(self):
        return f"Nome : {self.nome} - Indirizzo : {self.indirizzo} - Età : {self.eta}"
        

class Studente(Persona):
    def __init__(self, nome, indirizzo, eta, scuola, mediaVoti):
        super().__init__(nome, indirizzo, eta)
        self.__scuola = scuola
        self.__mediaVoti = mediaVoti

    @property
    def scuola(self):
        return self.__scuola
    
    @scuola.setter
    def scuola(self, scuola):
        if isinstance(scuola, str) and len(scuola) > 0:
            self.__scuola = scuola
        else:
            raise ValueError("Invalid insert")

    @property
    def mediaVoti(self):
        return self.__mediaVoti
    
    @mediaVoti.setter
    def mediaVoti(self,mediaVoti):
        if isinstance(mediaVoti, (int, float)):
            self.__mediaVoti = mediaVoti
        else:
            raise ValueError("Votes must be numbers")

    def __str__(self):
        return f"{super().__str__()} - Scuola : {self.scuola} - Media voti : {self.mediaVoti}"
    
class Lavoratore(Persona):
    def __init__(self, nome, indirizzo, eta, azienda, stipendio):
        super().__init__(nome, indirizzo, eta)
        self.__azienda = azienda
        self.__stipendio = stipendio

    @property
    def azienda(self):
        return self.__azienda
    
    @azienda.setter
    def azienda(self, azienda):
        if isinstance(azienda, str) and len(azienda) > 0:
            self.__azienda = azienda
        else:
            raise ValueError("Invalid insert")
    
    @property
    def stipendio(self):
        return self.__stipendio
    
    @stipendio.setter
    def stipendio(self,stipendio):
        if isinstance(stipendio, (int, float)):
            self.__stipendio = stipendio
        else:
            raise ValueError("Votes must be numbers")
        
    def __str__(self):
        return f"{super().__str__()} - Azienda : {self.azienda} - Stipendio : {self.stipendio}€"
    

janice = Persona("Janice", "Corso Siracusa", 33)
print(janice)


alessandro = Studente("Alessandro", "via luisetti 1000", 24, "Its Academy", 30)
print(alessandro)


tommaso = Lavoratore("Tommaso aka Giz", "sotto il pontos", 42, "Venditore di tessere ARCI", 12)
print(tommaso)