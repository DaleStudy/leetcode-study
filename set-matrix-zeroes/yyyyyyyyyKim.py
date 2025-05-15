class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 0이 있는 행, 열을 기록해두고 그 기록을 토대로 바꾸기(시간복잡도 O(m*n), 공간복잡도 O(m+n))
        m, n = len(matrix), len(matrix[0])
        # rows, cols = [] , []  -> 중복되어 들어갈 수 있음. 불필요함. 중복제거를 위해 set 사용.
        rows, cols = set(), set()

        # 0이 있는 행, 열 기록
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # 기록된 행 0으로 바꾸기
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0

        # 기록된 열 0으로 바꾸기
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0
