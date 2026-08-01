# 이렇게 푸는게 맞나..? 싶은데
# 일단 1차 제출하고 리팩토링 해보겠습니다. 🫠

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        total = sum(map(lambda k: len(k), matrix))
        answer = []
        visit = [[False] * len(matrix[0]) for _ in range(len(matrix))]

        def inRange(i, j):
            if not (0<=i<len(matrix)):
                return False
            if not (0<=j<len(matrix[0])):
                return False
            return True

        i, j = 0, 0
        answer.append(matrix[0][0])
        visit[0][0] = True
        while len(answer) < total:
            while inRange(i, j+1) and not visit[i][j+1]:
                visit[i][j+1] = True
                answer.append(matrix[i][j+1])
                j += 1
            
            while inRange(i+1, j) and not visit[i+1][j]:
                visit[i+1][j] = True
                answer.append(matrix[i+1][j])
                i += 1

            while inRange(i, j-1) and not visit[i][j-1]:
                visit[i][j-1] = True
                answer.append(matrix[i][j-1])
                j -= 1
            
            while inRange(i-1, j) and not visit[i-1][j]:
                visit[i-1][j] = True
                answer.append(matrix[i-1][j])
                i -= 1

        return answer
