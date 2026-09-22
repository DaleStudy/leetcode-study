class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        column = [1] * m

        for col in range(n - 1):

            for row in range(1, m):
                column[row] = column[row] + column[row - 1]

        return column[-1]
