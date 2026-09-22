# TC: O(NM)
# SC: O(N+M)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        m = len(matrix[0])

        row_set = set()
        col_set = set()

        for row in range(0, n):
            for col in range(0, m):
                if matrix[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)

        for row in range(0, n):
            for col in range(0, m):
                if row in row_set or col in col_set:
                    matrix[row][col] = 0

