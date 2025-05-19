class Solution:
    def setZeroes(self, matrix):
        first_row_zero = any(matrix[0][j] == 0 for j in range(len(matrix[0])))
        first_col_zero = any(matrix[i][0] == 0 for i in range(len(matrix)))

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
