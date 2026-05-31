# SC : O(m+n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])
        
        row_dict = {}
        col_dict = {}

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    row_dict[r] = True
                    col_dict[c] = True

        for r in range(m):
            for c in range(n):
                if r in row_dict or c in col_dict:
                    matrix[r][c] = 0
