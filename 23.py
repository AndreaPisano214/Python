def perfetto(n):
 if n == 0:
    return False

 divisori = []
 for i in range(1,n):
    if n % i == 0:
        divisori.append(i)

 return sum(divisori) == n
 n = int(raw_input( 'Inserisci un numero positivo: ' ))
 for i in range(0, n):
        if perfetto(i):
            print(i)