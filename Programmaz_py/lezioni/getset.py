# class Person:
#     def __init__(self,name):
#         self.__name = name #attributo privato
    # def set_name(self, name): #metodo setter
    #     if isinstance(name, str) and len(name) > 0: #validaz
    #         self.__name = name
    #     else:
    #         raise ValueError("Invalid name")

class Person:
    def __init__(self,name):
        self.__name = name #attributo privato

    @property
    def name(self): #getter method
        return self.__name
    
    @name.setter
    def name(self, name): #setter method
        if isinstance(name, str) and len(name) > 0: #validaz
             self.__name = name
        else:
             raise ValueError("Invalid name")
        
p = Person("Carlo")
print(p.name) #richiamo il getter -> 
p.name = "Carla" #richiamo il setter
print(p.name)
"""property permette di costruire attributi privati e costruire getter e setter
per lavorare in modo semplificato.

"""