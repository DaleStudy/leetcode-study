class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Hint 가이드에 따라 풀이

        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row = any(matrix[0][j] == 0 for j in range(n))
        first_col = any(matrix[i][0] == 0 for i in range(m))
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_col:
            for i in range(m):
                matrix[i][0] = 0
        if first_row:
            for j in range(n):
                matrix[0][j] = 0
