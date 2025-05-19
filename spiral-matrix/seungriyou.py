# https://leetcode.com/problems/spiral-matrix/

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        [Complexity]
            - TC: O(m * n) (m = row, n = col)
            - SC: O(1) (결과용 배열 res 제외)

        [Approach]
            시계 방향으로 순회하도록, 방문 표시 & 방향 전환을 하면서 res에 값을 저장한다.
            이때, 방문 표시를 inplace로 한다면 추가 공간을 사용하지 않을 수 있다.
        """

        # 방향: 우 -> 하 -> 좌 -> 상
        dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
        row, col = len(matrix), len(matrix[0])

        r, c, d = 0, 0, 0
        res = [matrix[r][c]]
        matrix[r][c] = "."

        while len(res) < row * col:
            # 다음 위치 후보 구하기
            nr, nc = r + dr[d], c + dc[d]

            # 다음 위치 후보가 (1) 범위를 벗어났거나 (2) 이미 방문한 위치라면, 방향 틀기
            if not (0 <= nr < row and 0 <= nc < col) or matrix[nr][nc] == ".":
                d = (d + 1) % 4
                nr, nc = r + dr[d], c + dc[d]

            # res에 추가 & 방문 표시
            res.append(matrix[nr][nc])
            matrix[nr][nc] = "."

            # 이동
            r, c = nr, nc

        return res
