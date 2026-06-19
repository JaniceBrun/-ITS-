"""Creazione classe Position"""

# classe position

class Position(object):
    """
    Rappresenta uno strumento finanziario in portafoglio
    Corrisponde ad un record nella tabella del db
    """
    #attributi di classe
    VALID_TYPES = ("etf", "etc", "etn", "azione", "obbligazione", "crypto")
    #mappa categorie macro
    MACRO_CATEGORIES = {
        "etf": "Investment",
        "etc": "Investment",
        "etn": "Investment",
        "azione": "Investment",
        "obbligazione": "Bonds & Money",
        "crypto": "Investment",
    }
    def __init__(self, id, ticker, name, type, currency="EUR"):
        self.__id = id
        self.__ticker = ticker
        self.__name = name
        self.__currency = currency
        self.__type = type #usa setter x validaz

    #getter id
    @property
    def id(self):
        return self.__id
    
    # getter setter ticker
    @property
    def ticker(self):
        return self.__ticker
    
    #setter controlla che sia str e non vuota e la porta a MAIUSC
    @ticker.setter
    def ticker(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Ticker deve essere una stringa non vuota")
        self.__ticker = value.upper()

    #setter e getter per name
    @property
    def name(self):
        return self.__name
    
    #setter controlla che name non sia vuota e sia str
    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("name deve essere una stringa non vuota")
        self.__name = value

    #getter e setter per currency
    @property
    def currency(self):
        return self.__currency
    
    #setter controlla currency sia str non vuota
    @currency.setter
    def currency(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("currency deve essere una stringa non vuota")
        self.__currency = value.upper()

    # getter e setter type
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, value):
        if value not in self.VALID_TYPES:
            raise ValueError("categoria non presente")
        self.__type = value

    #METODI DELLA CLASSE
    def from_dict(cls, data):
        """
        Metodo che crea oggetto position da un dict
        Converte i risultati delle query sql in oggetti
        """
        return cls(
            id = data["id"],
            ticker = data["ticker"],
            name = data["name"],
            type = data["type"],
            currency = data.get("currency", "EUR")
        )
    
    def to_dict(self):
        """
        Converte oggetto Position un un dict
        utile per serializzare output
        """
        return {
            "id": self.id,
            "ticker": self.ticker,
            "name": self.name,
            "type": self.type,
            "currency": self.currency
        }
    
    def macro_category(self):
        """
        Restituisce la categoria macro dello strumento
        """
        return self.MACRO_CATEGORIES.get(self.type, "Altro")






