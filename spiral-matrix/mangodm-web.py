from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        - Idea: 네 개의 포인터(left, right, top, bottom)를 활용하여 행렬의 바깥쪽부터 안쪽으로 순회한다.
            - left, right: 행렬의 왼쪽과 오른쪽 끝. 순회하면서 점점 좁혀진다.
            - top, bottom: 행렬의 위쪽과 아래쪽. 순회하면서 점점 좁혀진다.
        - Time Complexity: O(m*n), m, n은 각각 주어진 행렬(matrix)의 행과 열의 개수. 행렬의 모든 요소를 한번씩 접근한다.
        - Space Complexity: O(1), 결과 리스트(result)를 제외하고 포인터를 위한 상수 크기의 변수 이외의 추가 공간은 사용하지 않는다.
        """
        result = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result
