"""
Solution: 
    1) 좌우 상하의 경계를 좁혀가며 순회한다.
    2) 탈출 조건으로 result 의 사이즈가 matrix 의 원소 갯수가 같아지는지 확인한다.
    (탈출 조건을 좌우 상하 경계가 넘어가는 시험을 기준으로 삼은 솔루션을 봤지만, 정확히 이해는 되지 않아 사이즈 비교로 진행했습니다.)
Time: O(m * n)
Space: O(1)
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            if len(result) == len(matrix[0]) * len(matrix):
                break

            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            if len(result) == len(matrix[0]) * len(matrix):
                break

            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            if len(result) == len(matrix[0]) * len(matrix):
                break

            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

            if len(result) == len(matrix[0]) * len(matrix):
                break

        return result
