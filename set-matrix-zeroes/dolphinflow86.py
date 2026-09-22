# R is the number of rows, and C is the number of columns.
# TC: O(R * C) - scans each cell a constant number of times
# SC: O(1) - uses the first row and column as markers
class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_count = len(matrix)
        column_count = len(matrix[0])
        first_row_has_zero = any(matrix[0][col] == 0 for col in range(column_count))
        first_column_has_zero = any(matrix[row][0] == 0 for row in range(row_count))

        for row in range(1, row_count):
            for col in range(1, column_count):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, row_count):
            for col in range(1, column_count):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if first_row_has_zero:
            for col in range(column_count):
                matrix[0][col] = 0

        if first_column_has_zero:
            for row in range(row_count):
                matrix[row][0] = 0
