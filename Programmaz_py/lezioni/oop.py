

class Punto(object):
    """ Classe Punto di esempio
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translatePoint(self, t):
        return Punto (self.x +t, self.y +t) 

    def getDistance(self, P):
        return ((self.x - P.x)**2 + (self.y - P.y)**2)** 0.5
    

    def __str__(self):
        return str(self.x)+" "+str(self.y)
    
    # def stampa(self):
    #     return str(self.x)+" "+str(self.y)
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def setx(self, val):
        self.x = val
    def sety(self, val):
        self.y = val


p1 = Punto(2,3)
print(p1)
p2= p1.translatePoint(2)
print('Punto iniziale', p1)
print('Punto traslato', p2)

# print(p1.getx(), p1.gety())
# p1.setx(4)
# p1.sety(1)
# print(p1.getx(), p1.gety())
# print(p1.__doc__)
# print(p1.x, p1.y)
# print(p1.stampa())
# print(p1.__dict__)
# p1.altroAttributo=1 
# print(p1.__dict__)
# del(p1.y)
# print(p1.__dict__)
# p2 = Punto(4,2)
# print(p2.__dict__)

