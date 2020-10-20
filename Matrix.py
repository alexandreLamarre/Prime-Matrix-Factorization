class Matrix:
    """
    Square matrix
    """
    def __init__(self, matrix):
        assert len(matrix) == len(matrix[0]), "expected a square matrix"
        self.container = matrix

    def __mul__(self, other):
        if not isinstance(other, Matrix): return TypeError
        assert len(self.container) == len(other.container)
        matrix = []
        for i in range(len(self.container)):
            row = []
            for j in range(len(self.container)):
                row.append(self.dotProduct(self.getRow(i), other.getCol(j)))
            matrix.append(row)
        return Matrix(matrix)

    def getRow(self, i):
        return self.container[i][0:len(self.container)]

    def getCol(self, i):
        col = []
        for k in range(len(self.container)):
            col.append(self.container[k][i])

        return col

    def dotProduct(self, row, col):
        value = 0
        assert(len(row) == len(col))
        for k in range(len(row)):
            value += (row[k]*col[k])
        return value % 2

    def is_identity(self):
        for k in range(len(self.container)):
            if self.container[k][k] == 0: return False
        return True

    def __repr__(self):
        return str(self.container)


