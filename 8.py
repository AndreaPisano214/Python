def complementare(nucleodite):
    nucleodite = nucleodite.capitalize()
    if nucleodite == 'A': print('T')
    elif nucleodite == 'C': print('G')
    elif nucleodite == 'G': print('C')
    elif nucleodite == 'T': print('A')
nucleodite = input('(A,C,G,T):')
print(complementare(nucleodite))

def filamento_opposto(filamento):
    opposto = ''
    for nucleodite in filamento:
        opposto += complementare(nucleodite)
    return opposto    
