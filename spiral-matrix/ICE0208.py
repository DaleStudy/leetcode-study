class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISIT_NUM = 10000

        total = sum(map(lambda k: len(k), matrix))
        answer = []

        def isVisit(i, j):
            return matrix[i][j] == VISIT_NUM

        def setVisit(i, j):
            matrix[i][j] = VISIT_NUM

        def inRange(i, j):
            if not (0<=i<len(matrix)):
                return False
            if not (0<=j<len(matrix[0])):
                return False
            return True

        i, j = 0, 0
        answer.append(matrix[0][0])
        setVisit(0, 0)
        while len(answer) < total:
            while inRange(i, j+1) and not isVisit(i, j+1):
                answer.append(matrix[i][j+1])
                setVisit(i, j+1)
                j += 1
            
            while inRange(i+1, j) and not isVisit(i+1, j):
                answer.append(matrix[i+1][j])
                setVisit(i+1, j)
                i += 1

            while inRange(i, j-1) and not isVisit(i, j-1):
                answer.append(matrix[i][j-1])
                setVisit(i, j-1)
                j -= 1
            
            while inRange(i-1, j) and not isVisit(i-1, j):
                answer.append(matrix[i-1][j])
                setVisit(i-1, j)
                i -= 1

        return answer
