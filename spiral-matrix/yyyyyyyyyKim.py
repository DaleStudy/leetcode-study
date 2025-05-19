class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        answer = []

        # 경계값
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        
        # 시계방향으로 한 바퀴씩 돌기
        while top <= bottom and left <= right:

            # 오른쪽 이동
            for i in range(left,right+1):
                answer.append(matrix[top][i])
            top += 1

            # 아래로 이동
            for i in range(top,bottom+1):
                answer.append(matrix[i][right])
            right -= 1

            # 왼쪽 이동
            if top <= bottom:   # 위에서 top을 증가시켰기 때문에 다시 검사(아직 아래쪽에 행이 남아있는 경우에만 수행)
                for i in range(right,left-1,-1):
                    answer.append(matrix[bottom][i])
                bottom -= 1

            # 위로 이동
            if left <= right:   # 위에서 right를 감소시켰기 때문에 다시 검사(아직 왼쪽에 열이 남아있는 경우에만 수행)
                for i in range(bottom,top-1,-1):
                    answer.append(matrix[i][left])
                left += 1

        return answer
