class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero.append((i, j))
        
        for x, y in zero:
            for i in range(len(matrix[0])):
                matrix[x][i] = 0
            for i in range(len(matrix)):
                matrix[i][y] = 0
