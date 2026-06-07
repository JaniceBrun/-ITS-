# fh = open("file.txt", "r")
# print(fh)
# riga = fh.readline()
# while (riga != ''):
#     print(riga, end='')
#     riga = fh.readline()

righe = list()
righe.append("Prima riga di prova \n")
righe.append("secpnda riga \n")
righe.append("terza riga\n ")
righe.append("----------\n")
righe.append("ultima riga \n")

fh = open("fileout.txt", "w")

print(fh.writelines())

# for riga in righe:
#     fh.write(riga)

# fh = open("file.txt")
# for righe in fh:
#     print(righe, end= ' ')
# fh.close()