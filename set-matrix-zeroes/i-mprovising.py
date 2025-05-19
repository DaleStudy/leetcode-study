"""
Time, space complexity O(m * n)
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        i_indices = set()
        j_indices = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    i_indices.add(i)
                    j_indices.add(j)
        
        for i in i_indices:
            matrix[i] = [0 for _ in range(n)]
        for j in j_indices:
            for i in range(m):
                matrix[i][j] = 0
