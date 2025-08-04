"""
- 위쪽 행을 순회한 후, 상단 경계를 1 증가
- 오른쪽 열을 순회한 후, 우측 경계를 1 감소
- 아래쪽 행을 순회한 후, 하단 경계를 1 감소
- 왼쪽 열을 순회한 후, 좌측 경계를 1 증가

탈출 조건
1. 위쪽 행 순회를 마치고 상단 인덱스가 하단 인덱스보다 커지면
2. 오른쪽 열 순회를 마치고, 우측 인덱스가 좌측 인덱스보다 작아지면

TC: O(m * n) => 행렬의 저장된 모든 원소를 딱 1번씩만 접근, SC: O(1)
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1 # 행의 수 len(maxtrix)
        left, right = 0, len(matrix[0]) - 1 # 열의 수 len(maxtrix[0])

        output = []

        while top <= bottom and left <= right:
            # 위쪽 행 순회
            for c in range(left, right + 1):
                output.append(matrix[top][c])
            top += 1
            
            if top > bottom:
                break

            # 오른쪽 열 순회
            for r in range(top, bottom + 1):
                output.append(matrix[r][right])
            right -= 1

            if left > right:
                break

            # 아래쪽 행 순회
            for c in range(right, left - 1, -1):
                output.append(matrix[bottom][c])
            bottom -= 1

            # 왼쪽 열 순회
            for r in range(bottom, top - 1, -1):
                output.append(matrix[r][left])
            left += 1

        return output

# 2개의 포인터만 사용하는 풀이
"""
- 위쪽 행을 순회한 후, 열 인덱스를 1씩 증가
- 오른쪽 열을 순회한 후, 행 인덱스를 1씩 증가
- 아래쪽 행을 순회한 후, 열 인덱스를 1씩 감소
- 왼쪽 열을 순회한 후, 행 인덱스를 1씩 감소

인덱스
시작: (0, 0) => (행, 열)

탈출 조건
1. 위쪽 행 순회를 마치고 상단 인덱스가 하단 인덱스보다 커지면
2. 오른쪽 열 순회를 마치고, 우측 인덱스가 좌측 인덱스보다 작아지면
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n_rows, n_cols = len(matrix), len(matrix[0])
        row, col = 0, -1
        direction = 1

        output = []

        # 남아있는 열과 행의 개수가 0 보다 큰 동안
        while 0 < n_rows and 0 < n_cols:
            for _ in range(n_cols):
                col += direction
                output.append(matrix[row][col])
            n_rows -= 1

            for _ in range(n_rows):
                row += direction
                output.append(matrix[row][col])
            n_cols -= 1

            direction *= -1

        return output
    
