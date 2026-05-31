"""
# Approach
matrix를 순회하며 값이 0인 행과 열의 번호를 기록합니다.
기록한 것을 토대로 다시 matrix를 순회하며 0으로 채웁니다.

# Complexity
matrix의 행 크기를 M, 열 크기를 N이라고 할 때
- Time complexity: O(MN)
- Space complexity: O(M+N)
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows, cols = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        for x, row in enumerate(matrix):
            for y, value in enumerate(row):
                if value == 0:
                    zero_rows.add(x)
                    zero_cols.add(y)

        for x in zero_rows:
            for i in range(cols):
                matrix[x][i] = 0

        for y in zero_cols:
            for i in range(rows):
                matrix[i][y] = 0
