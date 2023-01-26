def eratostene(n):
 setaccio = range(2, n+1)
 primi = []
 while setaccio: 
    primi.append(setaccio[0])
    setaccio = filter(lambda x: x%primi[-1], setaccio)# finche' ci sono numeri nel setaccio
    return primi



print(eratostene)