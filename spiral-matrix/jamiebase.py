"""
# Approach
상하좌우 경계값을 설정하고 matrix을 순회하며 경계값을 줄여나갑니다.

# Complexity
matrix 크기의 가로를 M, 세로를 N이라고 할 때
- Time complexity: O(M*N)
- Space complexity: O(M*N)
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        start_row, start_col = 0, 0
        end_row, end_col = len(matrix) - 1, len(matrix[0]) - 1
        output = []

        while start_row <= end_row and start_col <= end_col:
            # 좌->우
            for col in range(start_col, end_col + 1):
                output.append(matrix[start_row][col])
            start_row += 1

            # 상->하
            for row in range(start_row, end_row + 1):
                output.append(matrix[row][end_col])
            end_col -= 1

            # 우->좌
            if start_row <= end_row:
                for col in range(end_col, start_col - 1, -1):
                    output.append(matrix[end_row][col])
                end_row -= 1

            # 하->상
            if start_col <= end_col:
                for row in range(end_row, start_row - 1, -1):
                    output.append(matrix[row][start_col])
                start_col += 1

        return output
