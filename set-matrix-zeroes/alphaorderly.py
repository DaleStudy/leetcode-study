"""
Time Complexity: O(m * n)
Space Complexity: O(1)

Approach:
- Use the first row and first column as markers to track which rows and columns should be zeroed.
- First, check if the original first row or first column should be zeroed by scanning them separately.
- Then, scan the rest of the matrix. If an element is zero, set its corresponding first row and first column positions to zero.
- Next, iterate through the matrix (excluding the first row and column) and set elements to zero if their corresponding first row or first column are zero.
- Finally, zero the first row and/or first column if initially flagged.
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW = len(matrix)
        COL = len(matrix[0])

        row_zero_check = any(matrix[0][c] == 0 for c in range(COL))
        col_zero_check = any(matrix[r][0] == 0 for r in range(ROW))

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, ROW):
            for c in range(1, COL):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if row_zero_check:
            for c in range(COL):
                matrix[0][c] = 0

        if col_zero_check:
            for r in range(ROW):
                matrix[r][0] = 0
