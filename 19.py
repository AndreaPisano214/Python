def spirale(n):
 mat = square( -1, n)
 x,y = 0,0 # cella iniziale
 dx,dy = 1,0 # incrementi iniziali
 for num in range(0,n**2):
 mat[y][x] = num # scrive il numero nella cella
 # evita di uscire dalla matrice o di scrivere su una cella piena
 if not(0 <= x+dx < n) or not(0 <= y+dy < n) or mat[y+dy][x+dx] is not -1:
 dx,dy = -dy,dx # ruota il vettore incremento
 # cambia cella
 x += dx
 y += dy

 return mat