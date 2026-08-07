class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_len = len(matrix)
        col_len = len(matrix[0])

        zero_row_set = set()
        zero_col_set = set()

        for r in range(row_len):
            for c in range(col_len):
                if matrix[r][c] == 0:
                    zero_row_set.add(r)
                    zero_col_set.add(c)

        for r in zero_row_set:
            for c in range(col_len):
                matrix[r][c] = 0

        for c in zero_col_set:
            for r in range(row_len):
                matrix[r][c] = 0
