from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for r in range(n):
            for c in range(m):
                if r in rows or c in cols:
                    matrix[r][c] = 0

