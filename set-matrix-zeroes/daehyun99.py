class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()

        for i in range(len(matrix)):
            if 0 in matrix[i]:
                row.add(i)
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 0:
                        col.add(j)

        for i in row:
            matrix[i] = [0] * len(matrix[0])
        
        for i in range(len(matrix)):
            if i in row:
                continue
            for j in range(len(matrix[0])):
                if j in col:
                    matrix[i][j] = 0

