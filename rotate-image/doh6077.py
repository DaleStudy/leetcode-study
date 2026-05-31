# https://leetcode.com/problems/rotate-image/
# 48. Rotate Image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # First Try - Thought process:
        # group values by column index (j) to rebuild rows
        # Brute force: create an extra 2D matrix and then copy it back into matrix
        # Needs optimization: this approach uses extra space
        matrix_result = [[] for _ in range(len(matrix))]
        for i in reversed(matrix):
            for j, value in enumerate(i):
                matrix_result[j].append(value)
        for r in range(len(matrix)):
            matrix[r] = matrix_result[r]
        
        # Youtube Solution - Transpose Operation + hr 
        # Swap i, js
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reflection
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
