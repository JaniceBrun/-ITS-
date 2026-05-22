"""Janice Brun
Esercizio: Mensa con Punti:
    Il programma deve stampare 
    -primi 5 euro
    -secondi 4 euro
    -dal secondo primo in poi sconto 20%
    - acqua gratis
    - bibita non acqua : +0,50
    output: [nome] - totale pranzo : xx. xx euro
"""


nome = input("inserisci il tuo nome: ")


primi = ['carbonara', 'lasagna', 'minestrone', 'tagliatelle', 'cannelloni']
secondi = ['tagliata', 'orata', 'costata', 'polpette', 'frittura']
bevande = ['bibita']

def calcolo_costi():
    
    ordini = ordine()
    contp = 0
    conts = 0
    contb = 0

    if len(ordini) > 0:
        for piatto in ordini:
            if piatto in primi:
                contp += 1
            elif piatto in secondi:
                conts += 1
            elif piatto in bevande:
                contb+= 1
    
    tot2 = 4 * conts
    tot1 = 0
    if contp > 0:
        tot1 += 4
        if contp > 1:
         tot1 += (contp - 1) * (4 * 0.8)

    tot3 = contb * 0.5

    totale = tot1 + tot2 + tot3
    return totale
    
    

def ordine():
    ordine = []
    piatto = input("Inserire uno alla volta i piatti desiderati(inserisci 'q' quando hai finito): ").lower()
    while piatto != 'q':
        ordine.append(piatto)
        piatto = input("Inserire uno alla volta i piatti desiderati(inserisci 'q' quando hai finito): ").lower()
    return ordine




def main():
    totale= calcolo_costi()
    print(f"Ciao {nome}. Il costo totale è di: {totale:.2f} euro")


if __name__ == '__main__':
    main()
