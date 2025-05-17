from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        # 첫 행에 0이 있는지 확인
        for col in range(cols):
            if matrix[0][col] == 0:
                first_row_zero = True
                break

        # 첫 열에 0이 있는지 확인
        for row in range(rows):
            if matrix[row][0] == 0:
                first_col_zero = True
                break

        # 마커 설정 (첫 행과 첫 열을 이용)
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # 마커에 따라 0으로 설정
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # 첫 행 처리
        if first_row_zero:
            for col in range(cols):
                matrix[0][col] = 0

        # 첫 열 처리
        if first_col_zero:
            for row in range(rows):
                matrix[row][0] = 0
