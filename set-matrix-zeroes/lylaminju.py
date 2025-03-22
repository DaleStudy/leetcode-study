'''
시간복잡도: O(m * n)
공간복잡도: O(1)
'''

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False  # Flag to check if the first row needs to be zeroed
        first_col_zero = False  # Flag to check if the first column needs to be zeroed

        # Check if the first row has any zeros
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if the first column has any zeros
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use the first row and column to mark rows and columns that need to be zeroed
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out cells based on markers in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero out the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
