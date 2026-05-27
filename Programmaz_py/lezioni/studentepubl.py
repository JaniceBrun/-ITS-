
class Studente(object):
    def __init__(self, nome, eta):
        self.nome = nome    #attributo di istanza
        self.eta = eta      #attributo di istanza
    def giorniEta(self):
        return self.eta * 365
    
studente1 = Studente("Carlo", 20)
print(studente1.nome, studente1.eta)
studente1.nome = "Mario"
studente1.eta = 21
print(studente1.nome,studente1.eta)
print(studente1.giorniEta())

