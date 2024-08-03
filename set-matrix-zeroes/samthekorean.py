# TC: O(m * n)
# SC: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Use first row and column to mark zero rows and columns
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # Set rows to zero based on marks in the first column
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0

        # Set columns to zero based on marks in the first row
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0

        # Handle the first row and column separately if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
