"""Autore: Janice Brun
esercizio : Calcolo costo VM
Chiedere:
nome studente
numero di ore utilizzo VM
costo orario (float)
Calcolare costo totale.
Se ore > 100 applicare sconto 10%.
Output:
<nome> - costo totale VM: XX.XX euro

"""

def inserimento():
    nome = input("Inserisci il tuo nome: ")
    ore_utilizzo = int(input("Quante ore hai utilizzato la tua VM?: "))
    costo_h = float(input("Quanto costa su base oraria?: "))

    return nome, ore_utilizzo, costo_h


def calcolo(ore, costo):
    totale = ore * costo
    if ore > 100:
        totale = totale * 0.9
        
    return totale
    
def main():

    nome, ore_uso, costo_orario = inserimento()
    totale = calcolo(ore_uso, costo_orario)

    print(f"{nome} - costo tolate VM {totale:.2f}")


if __name__ == '__main__':
    main()
    