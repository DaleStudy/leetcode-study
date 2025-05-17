'''
문제의도 : m x n 크디의 2차원 행렬에서 어떤 칸에 0이 있으면 그 칸이 속한 행과 열 전체를 0으로 바꿔야 함
조건 : 새로운 배열을 만들지 않고 원래 matrix에서 직접 바꿔야 함

해결방법 : 
1) 먼저 0이 있는 행과 열을 따로 기록해둠
2) 그 다음, 기록된 행과 열을 모두 0으로 만듬

시간 복잡도: O(m × n)
    행렬의 모든 칸을 한 번씩 확인하므로
공간 복잡도: O(m + n)
    0이 있는 행과 열 번호를 저장하는 데 최대 (행 개수 + 열 개수)만큼 공간이 필요하므로

'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]):
        rows = len(matrix)  # 행렬의 행 개수를 구함
        cols = len(matrix[0]) # 행렬의 열 개수를 구함
        zero_rows = set()  # 0이 있는 행 번호를 저장할 집함
        zero_cols = set()  # 0이 있는 열 번호를 저장할 집합

        # 모든 행과 열을 돌면서 0이 있으면 해당 행과 열 번호를 기록함
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # 0이 있는 행을 모두 0으로 바꿈
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

        # 0이 있는 열을 모두 0으로 바꿈
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0


                
