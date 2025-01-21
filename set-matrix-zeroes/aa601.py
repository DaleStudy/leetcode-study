# TC:O(n^2), SC:O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row = False
        first_col = False

        #첫번째 행, 열 flag
        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                first_row = True
        for c in range(len(matrix[0])):
            if matrix[0][c] == 0:
                first_col = True

        #그 이외의 행, 열 flag
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # 0으로 설정
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        # 첫번째 행과 열에 대해 각각 0으로 설정
        if first_row:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        if first_col:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
