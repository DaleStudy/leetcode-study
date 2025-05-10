'''
주어진 2차원 행렬을 나선형 순서로 반환하는 문제임
조건 : 위->오른쪽->아래->왼쪽을 반복적으로 순회하며 범위를 좁혀감

Example 1. 의 경우
1 2 3
4 5 6
7 8 9
단계	| top	bottom	left	right	|현재 행렬 상태	 | 동작 설명	                  
시작	   0	  2	      0	      2	      1 2 3
                                         4 5 6
                                         7 8 9	      위쪽 행() 처리 후 top=1로 증가	

2-1	      1	     2	     0	     2	     . . .
                                         4 5 6
                                         7 8 9	      오른쪽 열(열 2)의 행 1 처리: 6 추가	

2-2	      1	     2	     0	     2	     . . .
                                         4 5 6
                                         7 8 9	      오른쪽 열(열 2)의 행 2 처리: 9 추가	

끝	      1	      2	      0	      1	     . . .
                                         4 5 6
                                         7 8 9	      오른쪽 열 처리 끝, right=1로 감소	


'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]):
        if not matrix:
            return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            
            # 위쪽 행을 왼쪽 → 오른쪽으로 순회
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            
            # 다음부터 위쪽 행은 아래로 한 칸 이동
            top += 1
            
            # 오른쪽 열을 위쪽 → 아래쪽로 순회
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            
            # 다음부터 오른쪽 열은 왼쪽으로 한 칸 이동
            right -= 1
            
            # 아래쪽 행을 오른쪽 → 왼쪽으로 순회(행이 남아있을 때만)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            # 열이 남아 있을 때만 왼쪽 열을 아래쪽 → 위쪽으로 순회
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result



        