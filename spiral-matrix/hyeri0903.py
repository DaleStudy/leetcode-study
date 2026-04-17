class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        1.문제: 나선형으로 numbers return
        2.조건
        - m, n 길이 최소 = 1. 최대 = 10
        - 원소 값 최소 = -100, 최대 = 100
        3.풀이
        - 마지막 컬럼에 오면 index j change
        '''

        if len(matrix) == 1 and len(matrix[0]) == 1:
            return [matrix[0][0]]

        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        result = []

        while top <= bottom and left <= right:
            #left -> right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            #top -> bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
        
            #right -> left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            #bottom -> top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result
