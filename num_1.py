class Matrix:
    def __init__(self, m_1, m_2):
        self.m_1 = m_1
        self.m_2 = m_2

    def __add__(self):
        my_matrix = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
        for i in range(len(self.m_1)):
            for j in range(len(self.m_2)):
                my_matrix[i][j] = self.m_1[i][j] + self.m_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in my_matrix]))


a = Matrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]],
           [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]])
print(a.__add__())
