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

# definizione della classe Persona con attributi nome, indirizzo e età, metodi getter e setter, costruttore e metodo __str__

class Persona(object):
    """Classe che rappresenta una persona con nome, indirizzo e età, metodi getter e setter, costruttore e metodo __str__"""
    def __init__(self, nome: str, indirizzo: str, eta: int):
        """Costruttore della classe Persona che inizializza gli attributi nome, indirizzo e età"""
        self.__nome = nome
        self.__indirizzo = indirizzo
        self.__eta = eta

    @property
    def nome(self):
        """Metodo getter per l'attributo nome"""
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        """Metodo setter per l'attributo nome che verifica che il valore sia una stringa non vuota"""
        if isinstance(nome, str) and len(nome) > 0:
            self.__nome = nome
        else:
            raise ValueError("Invalid name")
        
    # getter e setter per indirizzo

    @property
    def indirizzo(self):
        """Metodo getter per l'attributo indirizzo"""
        return self.__indirizzo
    
    @indirizzo.setter
    def indirizzo(self, indirizzo: str):
        """Metodo setter per l'attributo indirizzo"""
        self.__indirizzo = indirizzo

    # getter e setter per età
        
    @property    
    def eta(self):
        """Metodo getter per l'attributo eta"""
        return self.__eta
    
    @eta.setter
    def eta(self, eta: int) -> int:
        """Metodo setter per l'attributo eta che verifica che il valore sia un numero intero positivo"""
        if isinstance(eta, int) and eta > 0:
            self.__eta = eta
        else:
            raise ValueError("Invalid age")
        
    def __str__(self) -> str:
        return f"Nome : {self.nome} - Indirizzo : {self.indirizzo} - Età : {self.eta}"
        
# definizione della classe Studente che deriva dalla classe Persona con attributi scuola e media voti, metodi getter e setter, costruttore e metodo __str__ derivato dalla classe Persona

class Studente(Persona):
    """Classe che rappresenta uno studente con scuola e media voti, metodi getter e setter, costruttore e metodo __str__ derivato dalla classe Persona"""
    def __init__(self, nome: str, indirizzo: str, eta: int, scuola: str, mediaVoti: float):
        """Costruttore della classe Studente che inizializza gli attributi nome, indirizzo, età, scuola e media voti"""
        super().__init__(nome, indirizzo, eta)
        self.__scuola = scuola
        self.__mediaVoti = mediaVoti

# getter e setter per scuola 

    @property
    def scuola(self):
        """Metodo getter per l'attributo scuola"""
        return self.__scuola
    
    @scuola.setter
    def scuola(self, scuola: str) -> str:
        """Metodo setter per l'attributo scuola che verifica che il valore sia una stringa non vuota"""
        if isinstance(scuola, str) and len(scuola) > 0:
            self.__scuola = scuola
        else:
            raise ValueError("Invalid insert")
# getter e setter per media voti

    @property
    def mediaVoti(self):
        """Metodo getter per l'attributo media voti"""
        return self.__mediaVoti
    
    @mediaVoti.setter
    def mediaVoti(self,mediaVoti: float) -> float:
        """Metodo setter per l'attributo media voti che verifica che il valore sia un numero"""
        if isinstance(mediaVoti, (int, float)):
            self.__mediaVoti = mediaVoti
        else:
            raise ValueError("Votes must be numbers")

# overriding del metodo __str__ per restituire nome, indirizzo, età, scuola e media voti

    def __str__(self):
        return f"{super().__str__()} - Scuola : {self.scuola} - Media voti : {self.mediaVoti}"

# definizione della classe Lavoratore che deriva dalla classe Persona con attributi azienda e stipendio, metodi getter e setter, costruttore e metodo __str__ derivato dalla classe Persona
   
class Lavoratore(Persona):
    """ Classe che rappresenta un lavoratore con azienda e stipendio, metodi getter e setter, costruttore e metodo __str__ derivato dalla classe Persona"""
    def __init__(self, nome, indirizzo, eta, azienda, stipendio):
        """Costruttore della classe Lavoratore che inizializza gli attributi nome, indirizzo, età, azienda e stipendio"""
        super().__init__(nome, indirizzo, eta)
        self.__azienda = azienda
        self.__stipendio = stipendio

# getter e setter per azienda

    @property
    def azienda(self):
        """Metodo getter per l'attributo azienda"""
        return self.__azienda
    
    @azienda.setter
    def azienda(self, azienda: str) -> str:
        """Metodo setter per l'attributo azienda che verifica che il valore sia una stringa non vuota"""
        if isinstance(azienda, str) and len(azienda) > 0:
            self.__azienda = azienda
        else:
            raise ValueError("Invalid insert")

# getter e setter per stipendio
    
    @property
    def stipendio(self):
        """Metodo getter per l'attributo stipendio"""
        return self.__stipendio
    
    @stipendio.setter
    def stipendio(self,stipendio: float) -> float:
        """Metodo setter per l'attributo stipendio che verifica che il valore sia un numero"""
        if isinstance(stipendio, (int, float)):
            self.__stipendio = stipendio
        else:
            raise ValueError("Stipendio must be a number")

# overriding del metodo __str__ per restituire nome, indirizzo, età, azienda e stipendio
         
    def __str__(self):
        return f"{super().__str__()} - Azienda : {self.azienda} - Stipendio : {self.stipendio}€"
    
 # istanzazione di un oggetto per ogni classe e test dei metodi __str__
  
janice = Persona("Janice", "Corso Siracusa", 33)
print(janice)


alessandro = Studente("Alessandro", "via luisetti 1000", 24, "Its Academy", 30)
print(alessandro)


tommaso = Lavoratore("Tommaso aka Giz", "sotto il pontos", 42, "Venditore di tessere ARCI", 12)
print(tommaso)