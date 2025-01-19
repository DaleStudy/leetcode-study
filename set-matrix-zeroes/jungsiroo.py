class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        """
        # Naive change : save rows and cols
        # SC : O(m+n)
        row_zero, col_zero = set(), set()
        
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)
        
        for i in range(rows):
            for j in range(cols):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0
        """

        # Constant Space Complexity using bitmasking
		# 0인 구간을 toggle 시켜놓고 확인하는 방법
        def is_on(number, k):
            return (number & (1<<k)) != 0
        
        row_zero, col_zero = 0, 0
        
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_zero |= (1 << i)
                    col_zero |= (1 << j)
        
        for i in range(rows):
            for j in range(cols):
                if is_on(row_zero, i) or is_on(col_zero, j):
                    matrix[i][j] = 0
        
