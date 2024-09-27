# 시간복잡도: O(m*n)
# 공간복잡도: O(m+n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        rows = set()
        cols = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for row in rows:
            for j in range(n):
                matrix[row][j] = 0

        for col in cols:
            for i in range(m):
                matrix[i][col] = 0
