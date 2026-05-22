"""Autore: Janice Brun
Esercizio: Gestione credenziali
Chiedere:
nome studente
password
La password è valida se:
almeno 8 caratteri
contiene almeno una lettera maiuscola
contiene almeno una minuscola
contiene almeno un numero
Stampare:
<nome> - Password valida oppure <nome> - Password non valida
"""

def controllo_credenziali():
    
    nome = input('Inserisci nome: ')
    pswd = input('Inserisci password: ')

    while pswd == pswd.lower or pswd == pswd.upper or len(pswd) < 8 or not any(crt.isdigit() for crt in pswd):
        print(f"{nome} - Password non valida")
        pswd = input('Inserisci nuova password: ')
    print(f"{nome} - Password valida")


if __name__ == '__main__':
    controllo_credenziali()