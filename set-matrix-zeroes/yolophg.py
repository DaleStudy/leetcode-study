# Time Complexity: O(m * n) - iterate through the matrix multiple times.
# Space Complexity: O(1) - no extra space is used apart from variables.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        
        # check if the first row contains any zero
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        # check if the first column contains any zero
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # use the first row and column to mark zero
        for i in range(1, m):  
            for j in range(1, n): 
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  
                    matrix[0][j] = 0 

        # update the matrix using the marks from the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0 

        # handle the first row separately if it initially had any zero
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0 

        # handle the first column separately if it initially had any zero
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0 
