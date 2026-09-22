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









# ---------

# SC : O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r_len , c_len = len(matrix), len(matrix[0])

        set_zero_first_col = any(matrix[r][0] == 0 for r in range(r_len))

        for r in range(r_len):
            for c in range(1, c_len):   # c는 1부터
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, r_len):
            for c in range(1, c_len):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0        

        if matrix[0][0] == 0:                  # 0행 먼저
            for c in range(c_len):
                matrix[0][c] = 0

            
        if set_zero_first_col:                 # 0열 나중
            for r in range(r_len):
                matrix[r][0] = 0         


