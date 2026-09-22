class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0] * n for _ in range(m)]
        matrix[0][0] += 1

        for x in range(m):
            for y in range(n):
                if x == 0 and y == 0:
                    continue
                elif x == 0:
                    matrix[x][y] += matrix[x][y-1]
                elif y == 0:
                    matrix[x][y] += matrix[x-1][y]
                else:
                    matrix[x][y] += (matrix[x][y-1] + matrix[x-1][y])
        return matrix[m-1][n-1]
