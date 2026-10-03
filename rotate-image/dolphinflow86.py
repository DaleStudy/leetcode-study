# N is the number of rows and columns in the matrix.
# TC: O(N^2) - reversing rows takes O(N^2) and transposing across diagonal takes O(N^2)
# SC: O(1) - in-place rotation with no extra memory allocation

from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1. Flip vertically (reverse rows)
        matrix.reverse()

        # 2. Transpose across main diagonal
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
