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

class AritmeticaDu(object):
    def __init__(self, operando1, operando2):
        self.__operando1 = operando1
        self.__operando2 = operando2

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

    def __str__(self):
        return f" operando 1 : {self.operando1}- operando 2 : {self.operando2}"