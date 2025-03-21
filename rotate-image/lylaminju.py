'''
시간 복잡도: O(n^2)
공간 복잡도: O(1)
'''
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n // 2):
            k = (n - 1) - i * 2

            for j in range(k):
                end = i + k

                matrix[i][i + j], matrix[i + j][end], matrix[end][end - j], matrix[end - j][i] = matrix[end - j][i], matrix[i][i + j], matrix[i + j][end], matrix[end][end - j]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Step 1: Transpose matrix (swap elements across diagonal)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()
