"""Janice Brun
Parsing Log Cloud
Il programma deve leggere il file access_log.txt contenete righe nel formato
DATA ORA IP METODO URL STATUS CODE_MS
Il programma deve calcolare e stampare:
1. numero totale richieste
2. numero richieste con status 200
3. numero richieste con status 404
4. IP che ha fatto più richieste
5. tempo medio di risposta (media di CODE_MS)
Output richiesto:
Report log - Studente: <nome>
Totale richieste: ...
Status 200: ...
Status 404: ...
IP più attivo: ...
Tempo medio risposta: ... ms
no librerie esterne
"""

def parsing(): 

    nome = input("inserisci il tuo nome: ")

    totale_richeste = 0
    status_200 = 0
    status_404 = 0
    somma_ms = 0
    ip_contuer = {}

    with open("access_log.txt", "r", encoding="utf-8") as f:
        

        for riga in f:
            riga = riga.strip()
            if not riga:
                continue
            
            totale_richeste += 1
            sezione = riga.split()

            data = sezione[0]
            ora = sezione[1]
            ip = sezione[2]
            metodo = sezione[3]
            url = sezione[4]
            status = int(sezione[5])
            tempo_ms = int(sezione[6])
            
            if status == 200:
                status_200 += 1
            elif status == 404:
                status_404 += 1

            if ip not in ip_contuer:
                ip_contuer[ip] = 0
            ip_contuer[ip] += 1

            somma_ms += tempo_ms

        temp_medio = somma_ms / totale_richeste
            
        ip_top = max(ip_contuer, key=ip_contuer.get)

    print(f"""
        Report log - Studente: {nome}
        Totale richieste: {totale_richeste}
        Status 200: {status_200}
        Status 404: {status_404}
        Ip più attivo: {ip_top}
        Tempo medio risposta: {temp_medio} ms
""")
    
if __name__ == '__main__':
    parsing()