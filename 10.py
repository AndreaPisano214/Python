v1 = (1,2,3,4,5)
v2 = (6,7,8,9,10)
mat = []
for i, x1 in enumerate(v1):
    mat.append([])
    for x2 in v2:
        mat[i].append(x1*x2)
for row in mat:
    print(row)