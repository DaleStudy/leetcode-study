"""TC: O(m * n), SC: O(m + n)

아이디어:
모든 칸을 훑으면서 어떤 row, column을 0으로 바꿔줘야 하는지 찾은 다음 0으로 바꾸는 시행을 한다.

SC:
- 바꿔야 하는 column, row를 set으로 관리. 각각 O(m), O(n)이므로 종합하면 O(m + n).

TC:
- 모든 칸을 돌면서 어떤 column과 row를 0으로 바꿔야 하는지 체크한다. O(m * n).
- 0으로 바꿔야 하는 모든 column을 0으로 바꾼다. 모든 column을 다 0으로 바꿔야 할 경우 모든 칸에
  접근해서 0을 넣어주어야 하므로 O(m * n).
- row도 column과 똑같이 접근 가능하다. O(m * n).
- 종합하면 O(m * n).
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        col_to_change, row_to_change = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    col_to_change.add(i)
                    row_to_change.add(j)
        for i in col_to_change:
            for j in range(n):
                matrix[i][j] = 0

        for j in row_to_change:
            for i in range(m):
                matrix[i][j] = 0
