nomi=('Numa','Tullio','Paolo')
cognomi=('Figo','Brutto','Bello')
l=[]
for nome,cognome in zip(nomi,cognomi):
    l.append({'Nome': nome,'Cognome': cognome})
print(l)