"""
Solution: 
    1) matrix를 순회하면서 0을 찾는다. 
    2) 0일 경우 rows, cols set에 각 인덱스를 넣는다.
    3) rows, cols 를 순회하면서 해당하는 row, col을 0으로 만들어준다.
Time: O(nm) = O(nm) (순회) + 최대 O(nm) + 최대 O(nm)
Space: O(n + m)
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rows = set()
        cols = set()
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in rows:
            for j in range(COLS):
                matrix[i][j] = 0

        for j in cols:
            for i in range(ROWS):
                matrix[i][j] = 0
