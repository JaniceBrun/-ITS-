"""
    Autore: Janice Brun
    Data: 29/05/2026
    Titolo: Creare una classe AritmeticaDue con attributi operando1 e operando2. Definire il
    costruttore utilizzando parametri con valori predefiniti e il metodo str.
    Aggiungere due metodi uno che restituisca la differenza e l'altro il prodotto dei due
    operandi. Implementare un terzo metodo che permetta il confronto tra il risultato del
    prodotto di due oggetti AritmeticaDue (in sostanza indicare se il prodotto è maggiore di
    quello calcolato nell'oggetto AritmeticaDue passato come parametro).
    Derivare dalla classe AritmeticaDue la classe AritmeticaTre aggiungendo l'attributo
    operando3. Ridefinire il costruttore, il metodo str e i tre metodi differenza, prodotto e
    confronto. Aggiungere un metodo per il calcolo della somma di tutti gli attributi.
    Provare le classi e i metodi implementati.


"""
# definizione della classe AritmeticaDue con attributi operando1 e operando2, costruttore con parametri predefiniti, metodo str, metodi per differenza, prodotto e confronto

class AritmeticaDu(object):
    """Classe che rappresenta un oggetto con due operandi, metodi per differenza, prodotto e confronto"""
    def __init__(self, operando1=10 , operando2=20):
        """Costruttore della classe AritmeticaDu che inizializza gli attributi operando1 e operando2 con valori predefiniti"""
        self.__operando1 = operando1
        self.__operando2 = operando2

# getter e setter per operando1 e operando2

    @property
    def operando1(self):
        """Metodo getter per l'attributo operando1"""
        return self.__operando1
    
    @operando1.setter
    def operando1(self, operando1):
        """Metodo setter per l'attributo operando1 che verifica che il valore sia un numero positivo"""
        if isinstance(operando1, (int, float)) and operando1 > 0:
            self.__operando1 = operando1
        else:
            raise ValueError("Valore invalido")

    @property
    def operando2(self):
        """Metodo getter per l'attributo operando2"""
        return self.__operando2
    
    @operando2.setter
    def operando2(self, operando2):
        """Metodo setter per l'attributo operando2 che verifica che il valore sia un numero positivo"""
        if isinstance(operando2, (int, float)) and operando2 > 0:
            self.__operando2 = operando2
        else:
            raise ValueError("Valore invalido")

    # metodo per la differenza che restituisce la differenza tra il maggiore e il minore dei due operandi

    def differenza(self):
        """Metodo che restituisce la differenza tra il maggiore e il minore dei due operandi"""
        op1 = min(self.operando1, self.operando2)
        op2 = max(self.operando1, self.operando2)
        return op2 - op1

    # metodo per il prodotto che restituisce il prodotto dei due operandi

    def prodotto(self):
        """Metodo che restituisce il prodotto dei due operandi"""
        return self.operando1 * self.operando2
    
    # metodo per il confronto tra il prodotto di due oggetti AritmeticaDu

    def confrontaProdotto(self, oggetto2: AritmeticaDu):
        """Metodo che confronta il prodotto di due oggetti AritmeticaDu"""
        if self.prodotto() > oggetto2.prodotto():
            return f"{self} > {oggetto2}"
        else:
            return f"{self.prodotto()} < {oggetto2.prodotto()}"
        
    # overriding del metodo __str__ per restituire una stringa con i valori dei due operandi

    def __str__(self):
        return f" operando1 : {self.operando1} - operando2 : {self.operando2}"
    
# definizione della classe AritmeticaTre che deriva dalla classe AritmeticaDu con attributo operando3, metodi getter e setter, costruttore, metodo str, metodi per differenza, prodotto e confronto

class AritmeticaTre(AritmeticaDu):
    """Classe che rappresenta un oggetto con tre operandi, metodi per differenza, prodotto, confronto e somma"""
    def __init__(self, operando1=10, operando2=20, operando3=30):
        """Costruttore della classe AritmeticaTre che inizializza gli attributi operando1, operando2 e operando3 con valori predefiniti"""
        super().__init__(operando1, operando2)
        self.__operando3 = operando3

# getter e setter per operando3

    @property
    def operando3(self):
        """Metodo getter per l'attributo operando3"""
        return  self.__operando3
    
    @operando3.setter
    def operando3(self, operando3):
        """Metodo setter per l'attributo operando3 che verifica che il valore sia un numero positivo"""
        if isinstance(operando3, (int, float)) and operando3 > 0:
            self.__operando3 = operando3
        else:
            raise ValueError("Valore invalido")

    # overriding del metodo __str__ per restituire una stringa con i valori dei tre operandi

    def __str__(self):
        return f"{super().__str__()} - Operando3 : {self.operando3}"
    
    # overriding dei metodi differenza, prodotto e confronto per tenere conto del terzo operando

    def prodotto(self):
        """Metodo che restituisce il prodotto dei tre operandi"""
        return (super().prodotto()) * self.operando3

    # metodo per il confronto tra il prodotto di due oggetti AritmeticaTre

    def differenza(self):
        """Metodo che restituisce la differenza tra il maggiore e il minore dei tre operandi"""
        lista_operandi = sorted([self.operando1, self.operando2, self.operando3])
        return lista_operandi[-1] - lista_operandi[0]

    # metodo per il confronto tra il prodotto di due oggetti AritmeticaTre

    def somma(self):
        """Metodo che restituisce la somma dei tre operandi"""
        return self.operando1 + self.operando2 + self.operando3
    
oggetto1 = AritmeticaDu(4,5)
print(oggetto1)
# print(oggetto1.differenza())
# print(oggetto1.prodotto())
oggetto2 = AritmeticaDu(2,3)
# print(oggetto1.confrontaProdotto(oggetto2))

oggetto3 = AritmeticaTre(8,9)
print(oggetto3)
print(oggetto3.confrontaProdotto(oggetto2))
print(oggetto3.somma())
print(oggetto3.differenza())
print(oggetto3.prodotto())