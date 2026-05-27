"""Autore : Janice brun
   Data   : 25/05/2026
   Testo  : 1 - Creare una classe Calcolo con un costruttore di default (senza parametri) che consenta
   di eseguire vari calcoli su numeri interi.
   2 - Creare un metodo chiamato Factorial() che permetta di calcolare il fattoriale di un
   intero. Testare il metodo istanziando la classe.
   3 - Creare un metodo chiamato Sum() che consenta di calcolare la somma dei primi n
   interi 1 + 2 + 3 + .. + n. Prova questo metodo.
   4 - Creare un metodo tableMult() che crea e visualizza la tabellina di un dato intero. Quindi
   creare un metodo allTablesMult() per visualizzare tutte le tabelline di numeri interi 1, 2, 3,
    ..., 9.
"""

class Calcolo(object):
    def __init__(self):
        pass

    def factorial(self, numero):
        for base in range(1, numero + 1):
            base = 1 * base
        return base

    def sum(self, n):
        for numero in range(1, n + 1):
            numero += numero
        return numero
    
    def tableMult(self, numero, moltiplicatore):
        multipli = []      
        for i in range(1, moltiplicatore +1) :
            risultato = (numero * i)
            multipli.append(risultato)
        return multipli
    





calc = Calcolo()
print(calc.sum(3))
print(calc.tableMult(2,10))
print(calc.factorial(5))