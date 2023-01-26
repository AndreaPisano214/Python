v1 = (1,2,3,4,5)
v2 = (6,7,8,9,10)
for x1 in v1:
    for x2 in v2:
        mat = [[x1*x2 for x2 in v2] for x1 in v1]

def stampa_matrice(mat):
    for row in mat:
        for num in row:
            print('%3i'%num,)




#non funziona!!!!