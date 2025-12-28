class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Time Complexity(n^2)
        # Space Complexity O(1)
        row = len(matrix)
        col = len(matrix[0])
        row_zero = False

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True
        
        for r in range(1, row):
            for c in range(1, col):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
 
        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0
        
        if row_zero:
            for c in range(col):
                matrix[0][c] = 0
