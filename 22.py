def conta_caratteri(s):
    conteggio = {}
    for c in s:
        if c in conteggio:
            conteggio[c] += 1
        else:
            conteggio[c] = 1
    return conteggio

conta_caratteri('aiuola')
{'a':2, 'i':1, 'u':1, 'o':1, 'l':1}