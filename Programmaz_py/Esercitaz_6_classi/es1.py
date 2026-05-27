"""Autore : Janice brun
   Data   : 25/05/2026
   Testo  : Creare una classe Insegnante con attributi nome, età e stipendio, dove stipendio deve
   essere un attributo privato.
   Costruire tutti i metodi getter e setter per gli attributi (anche per quelli pubblici)
   Effettuare l'overriding del metodo __str__ in maniera tale che restituisca gli attributi nome e
   età.
   Provare la classe istanziando almeno due oggetti.
   """
# creazione della classe Insegnante con attributi nome, età e stipendio (privato)

class Insegnante(object):
    """Classe che rappresenta un insegnante con nome, età e stipendio (privato)"""
    def __init__(self, nome: str, eta: int, stipendio: float):

        self.nome = nome
        self.eta = eta
        self.__stipendio = stipendio

    # getter e setter per nome

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
        
    # getter e setter per stipendio (privato)
        
    @property
    def stipendio(self):
        """Metodo getter per l'attributo stipendio"""
        return self.__stipendio        
        
    @stipendio.setter
    def stipendio(self, stipendio):
        """Metodo setter per l'attributo stipendio che verifica che il valore sia un numero"""
        if isinstance(stipendio, (float, int)):
            self.__stipendio = stipendio
        else:
            raise ValueError("Invalid salary")
    
    # overriding del metodo __str__ per restituire nome e età

    def __str__(self):
        return F"Nome : {self.nome}, eta: {self.eta} anni"
    
# istanziazione di due oggetti Insegnante e test dei metodi getter, setter e __str__
    
insegnate1 = Insegnante("Marco", 25, 2000)  

print(insegnate1.nome)
print(insegnate1.eta)
print(insegnate1.stipendio)

insegnate1.nome = "MAtteo"
insegnate1.eta = 50
insegnate1.stipendio = 1000.0

print(insegnate1)

insegnate2 = Insegnante("Alessandro", 50, 1600.5)

print(insegnate2.nome)
print(insegnate2.eta)
print(insegnate2.stipendio)

insegnate2.nome = "Edoardo"
insegnate2.eta = 44
insegnate2.stipendio = 1002.2

print(insegnate2)