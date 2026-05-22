"""Autore: Janice Brun
Esercizio: File filter avanzato
File: es4_file_filtra.py
Uguale all'es3 file precedente, ma:
file input: input.txt
file output deve chiamarsi: output_<nome>.txt
Esempio: output_Mauro.txt
Scrivere solo le righe che contengono i caratteri della stringa s in ordine.
"""

def cerca_in_file(line, s):
    
    i = 0
    for carattere in line:
        if i < len(s) and carattere == s[i]:
            i += 1
    return i == len(s)
    

def main():
    nome = input("Inserisci il tuo nome: ").strip()
    s = input("Inserisci la stringa da trovare: ").strip()
    
    input_file = "input.txt"
    outfile = f"output_{nome}.txt"

    with open("input.txt", "r", encoding="utf-8") as infile, open(f"output_{nome}.txt", "w", encoding="utf-8") as outfile:
        for line in infile:
            if cerca_in_file(line.strip(), s):
                outfile.write(line)
    
    print(f"File filtrato creato: output_{nome}.txt")

if __name__ == "__main__":
    main()