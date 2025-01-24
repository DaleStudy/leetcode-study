'''
# 73. Set Matrix Zeroes
# solution reference: https://www.algodale.com/problems/set-matrix-zeroes/
'''
class Solution:
    '''
    ### TC is O(m * n):
    -  iterating through every cells, to find the zero cells. = O(m * n) 1️⃣
    -  iterating through every cells, to update the rows. = O(m * n) 2️⃣
    -  iterating through every cells, to update the columns. = O(m * n) 3️⃣

    ### SC is O(m + n):
    - using each set to store the rows(O(m)) and columns(O(n)) that have zero. = O(m + n)
    '''
    def setZeroesWithSet(self, matrix: List[List[int]]) -> None:
        zero_rows = set() # SC: O(m)
        zero_cols = set() # SC: O(n)

        for r in range(len(matrix)): # TC: O(m * n)
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for r in zero_rows: # TC: O(m * n)
            for i in range(len(matrix[0])):
                matrix[r][i] = 0

        for c in zero_cols: # TC: O(m * n)
            for i in range(len(matrix)):
                matrix[i][c] = 0

    '''
    ### TC is O(m * n):
    - check if the first row or column has zero. = O(m + n)
    - iterating through every cells, if it has zero, mark the first row and column. = O(m * n) 1️⃣
    - update the matrix based on the marks(0) in the first row and column. = O(m * n) 2️⃣
    - if the first row or column has zero, iterating through every cells, in the first row or column and updating it. = O(m + n) 

    ### SC is O(1):
    - using the first_row_has_zero and first_col_has_zero to store the zero information. = O(1)
    '''
    def setZeroesWithMarkerAndVariable(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols)) # TC: O(n), SC: O(1)
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows)) # TC: O(m), SC: O(1)

        for r in range(1, rows): # TC: O(m * n)
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, rows): # TC: O(m * n)
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row_has_zero: 
            for c in range(cols): # TC: O(n)
                matrix[0][c] = 0

        if first_col_has_zero:
            for r in range(rows): # TC: O(m)
                matrix[r][0] = 0
