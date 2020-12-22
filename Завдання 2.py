# Виведення на екран кількості вершин;
# виведення на екран ребер графа;
# додавання нового ребра;
# видалення ребра;
# пошук шляхів між двома заданими вершинами.



class Grath:
    def __init__(self, _manyTop , _matrix):
        self.manyTop = 6
        self.matix = [[0, 1, 1, 0, 1, 0],
                  [1, 0, 0, 1, 0, 0],
                  [1, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1, 0],
                  [1, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0]]

    @property
    def printMatix(self):
        for i in range(self.manyTop):
            print(self.matix[i], end='\n')

    @property
    def printManyTop(self):
        print('Tops = ', self.manyTop)

    def addNewRib(self, x, y):
        self.matix[x][y] = 1
        self.matix[y][x] = 1

        for i in range(self.manyTop):
            print(self.matix[i], end='\n')

    def delRib(self, x ,y):
        self.matix[x][y] = 0
        self.matix[y][x] = 0

        for i in range(self.manyTop):
            print(self.matix[i], end='\n')

    def findingWay(self, x, y):
        if self.matix[x][y] == 1:
            print('The path exist!')
        else:
            print('Sorry. The path does not exist.')

#------------------------

k = input('You have write matix? (y/n): ')
if k == 'n':
    mmatix = [[0, 1, 1, 0, 1, 0],
        [1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]]

    g = Grath(6, mmatix)
    g.findingWay(0, 1)
else:
    tops = int(input('Tops = '))
    mmatix = []
    mmatix = [[int(input("matix[{0}][{1}]=".format(i,j)))  for j in range(tops)] for i in range(tops)]

t = Grath()
t.addNewRib(5,2)
t.delRib(5,2)
t.findingWay(5,2)