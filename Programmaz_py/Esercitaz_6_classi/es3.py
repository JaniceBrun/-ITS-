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
# creazione della classe Calcolo con un costruttore di default, metodo factorial, metodo sum, metodo tableMult, metodo allTablesMult

class Calcolo(object):
    """Classe che rappresenta un calcolo con un costruttore di default, metodo factorial, metodo sum, metodo tableMult, metodo allTablesMult"""
    def __init__(self):
        pass

    def factorial(self, numero: int) -> int:
        """Metodo che calcola il fattoriale di un intero
        
        param numero: intero di cui calcolare il fattoriale
        
        return: fattoriale di numero"""
        fattoriale = 1
        for base in range(1, numero + 1):
            fattoriale *= base
        return fattoriale

    def sum(self, n: int) -> int:
        """Metodo che calcola la somma dei primi n interi
        
        param n: intero che indica fino a quale numero calcolare la somma
        
        return: somma dei primi n interi"""
        risultato_somma = 0
        for numero in range(1, n + 1):
            risultato_somma += numero
        return risultato_somma
    
    def tableMult(self, numero: int, moltiplicatore: int) -> list:
        """Metodo che crea e visualizza la tabellina di un dato intero
        
        param numero: intero per cui creare la tabellina
        param moltiplicatore: intero che indica fino a quale numero moltiplicare
        
        return: lista dei risultati della tabellina"""
        multipli = []      
        for i in range(1, moltiplicatore +1) :
            risultato = (numero * i)
            multipli.append(risultato)
        return multipli
    
    def alltablesMult(self) -> dict:
        """Metodo che visualizza tutte le tabelline di numeri interi da 1 a 9
        
        param: nessuno
        
        return: dizionario con chiave il numero e valore la lista dei risultati della tabellina"""
        tabelline_dict = {}
        for numero in range(1,10):
            tabelline_dict[numero] = self.tableMult(numero, 10)
        
        # for numero, tabellina in tabelline_dict.items():
        #     print(f"Tabellina del {numero}: {tabellina}")
        # return
        return tabelline_dict





calc = Calcolo()
print(calc.sum(15))
print(calc.tableMult(2,10))
print(calc.factorial(5))
print(calc.alltablesMult())