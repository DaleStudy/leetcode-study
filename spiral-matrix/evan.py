from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        result = []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while left <= right and top <= bottom:
            # Traverse from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            # Move the top boundary down
            top += 1

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            # Move the right boundary to the left
            right -= 1

            if top <= bottom:
                # Traverse from right to left
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                # Move the bottom boundary up
                bottom -= 1

            if left <= right:
                # Traverse from bottom to top
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                # Move the left boundary to the right
                left += 1

        return result
