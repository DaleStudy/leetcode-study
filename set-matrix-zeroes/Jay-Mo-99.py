        #해석
        # matrix의 모든 element를 검사한다, 만약 0을 발견하면 해당 element와 같은 row와 col을 가진 element를 "a" 로 바꾼다.
        # 두번째로 matrix의 모든 element를 검사한다, 만약 a를 발견하면 이를 0으로 바꾼다.  


        #Big O
        #- N: row의 크기(matrix 행의 갯수)
        #- K: col의 크기(matrix 열의 갯수 )

        #Time Complexity: O(N*K*(N+K))
        #- for nested loop : 행의 갯수(N) 당 열의 갯수만큼(K) 루프 작동 -> O(N*K)
        #   - 최악의 경우, 첫번째 루프에서 for i in range(rows)가 M번 발동, for j in range(cols)가 N번 발동 -> O(N+K) 

        #Space Complexity: O(1)
        #- rows, cols: 변수의 할당과 업데이트는 상수 취급한다 -> O(1)
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0]) #rows와 cols에 matrix의 좌표 부여 
        
        # 1차 matrix 순회: 0을 발견하면, 그 element의 같은 행과 열의 0이 아닌 수를 임시 값 "a"로 바꾸기
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # 해당 행과 열의 0이 아닌 모든 값을 임시로 "a"로 변경
                    for i in range(rows):  # 해당 열의 모든 값
                        if matrix[i][c] != 0:
                            matrix[i][c] = "a"
                    for j in range(cols):  # 해당 행의 0이 아닌 모든 값을 "a"로 변경
                        if matrix[r][j] != 0:
                            matrix[r][j] = "a"
        
        # 2차 matrix순회: "a"를 가진 수를 0으로 바꿔준다.
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "a":
                    matrix[r][c] = 0



