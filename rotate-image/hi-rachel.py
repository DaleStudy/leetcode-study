"""
https://leetcode.com/problems/rotate-image/description/

TC: O(n^2)
SC: O(1)
"""

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top, bottom = 0, len(matrix) - 1

        while top < bottom:
            left, right = top, bottom

            for i in range(bottom - top):
                topLeft = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = topLeft

            top, bottom = top + 1, bottom - 1
            
