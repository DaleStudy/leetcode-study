class Solution:
    # Time: O(m*n), m = len(matrix), len(matrix[0])
    # Space: O(m+n)
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_zeros, col_zeros = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_zeros.add(i)
                    col_zeros.add(j)
        for r in row_zeros:
            for j in range(len(matrix[0])):
                matrix[r][j] = 0
        for c in col_zeros:
            for i in range(len(matrix)):
                matrix[i][c] = 0
