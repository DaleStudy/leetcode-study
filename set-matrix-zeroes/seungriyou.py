# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List

class Solution:
    def setZeroes_slow(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        [Complexity]
            - TC: O(m * n * (m + n)) -> too slow...
            - SC: O(1)

        [Approach]
            다음의 두 단계를 inplace로 수행한다.
                1. 모든 cell을 순회하며, 0을 발견하면 해당 row와 column의 값을 (0인 cell을 제외하고) 모두 #로 바꾼다.
                2. 다시 모든 cell을 순회하며, #을 모두 0으로 바꾼다.
        """

        m, n = len(matrix), len(matrix[0])

        def set_row_col(r, c):
            for _r in range(m):
                # 0이 아닌 경우에만 "#"으로 바꿔야 함 **
                if matrix[_r][c] != 0:
                    matrix[_r][c] = "#"

            for _c in range(n):
                if matrix[r][_c] != 0:
                    matrix[r][_c] = "#"

        # 1. 0을 발견하면 해당 row & column을 "#"으로 바꾸기
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    # row & column을 "#"으로 바꾸기
                    set_row_col(r, c)

        # 2. "#"을 모두 0으로 바꾸기
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "#":
                    matrix[r][c] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        [Complexity]
            - TC: O(m * n)
            - SC: O(1)

        [Approach]
            matrix의 첫 번째 row와 column을 flag 기록 용도로 사용한다면, space를 O(1)로 유지하면서 time도 최적화할 수 있다.
                - 첫 번째 row: 각 column에 0이 있었다면, 해당 column의 칸에 0으로 기록
                - 첫 번째 column: 각 row에 0이 있었다면, 해당 row의 칸에 0으로 기록
            이렇게 첫 번째 row와 column을 flag 기록용으로 쓰기 전에, 해당 row와 column에 0이 있었는지 여부를 미리 확인해야 함에 유의한다.
            전체 흐름은 다음과 같다:
                1. 첫 번째 row와 column에 0이 존재하는지 여부 확인
                2. 두 번째 row와 column 부터 0이 존재하는 칸에 대해 첫 번째 row와 column에 flag 기록
                3. 첫 번째 row와 column의 flag 값을 기반으로, 0 채우기
                4. 1번에서 구해둔 값으로도 0 채우기
        """

        m, n = len(matrix), len(matrix[0])

        # 1. 첫 번째 row와 column에 0이 존재하는지 여부 확인
        has_zero_in_first_row = any(matrix[0][_c] == 0 for _c in range(n))
        has_zero_in_first_col = any(matrix[_r][0] == 0 for _r in range(m))

        # 2. 두 번째 row와 column 부터 0이 존재하는 칸에 대해 첫 번째 row와 column에 flag 기록
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        # 3. 첫 번째 row와 column의 flag 값을 기반으로, 0 채우기
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # 4. 1번에서 구해둔 값으로도 0 채우기
        if has_zero_in_first_row:
            for _c in range(n):
                matrix[0][_c] = 0

        if has_zero_in_first_col:
            for _r in range(m):
                matrix[_r][0] = 0
