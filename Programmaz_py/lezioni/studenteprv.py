class Studente(object):
    def __init__(self, nome, eta):
        self.__nome = nome    #attributo di istanza
        self.__eta = eta      #attributo di istanza
    def giorniEta(self):     #metodo 
        return self.__eta * 365
"""senza get/set non si può accedere agli arrtibuti"""

studente1 = Studente("Carlo",20)
#-------------------------------------------

# print(studente1.__nome)
print(dir(studente1))
print("\n"+studente1._Studente__nome)