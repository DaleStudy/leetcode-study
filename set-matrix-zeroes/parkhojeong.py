class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_len = len(matrix)
        col_len = len(matrix[0])
        MARKER = sys.maxsize

        def dfs(row, col, d_row, d_col):
            if not (0 <= row < row_len and 0 <= col < col_len):
                return

            if matrix[row][col] == 0:
                return

            matrix[row][col] = MARKER
            dfs(row + d_row, col + d_col, d_row, d_col)

        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:

                    matrix[row][col] = MARKER
                    dfs(row + 1, col, 1, 0)
                    dfs(row - 1, col, -1, 0)
                    dfs(row, col + 1, 0, 1)
                    dfs(row, col - 1, 0, -1)

        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == MARKER:
                    matrix[row][col] = 0
