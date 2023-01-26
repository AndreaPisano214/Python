class Matrice:
    def __init__(self, mat):
        self.mat = mat
def stampa(self):
    for row in self.mat:
        for num in row:
            print ('%3i' % num,)
print

m = Matrice([[ 1,2,3],[4,5,6],[7,8,9]])
m.stampa()