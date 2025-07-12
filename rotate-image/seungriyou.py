# https://leetcode.com/problems/rotate-image/

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        [Complexity]
            - TC: O(n^2) (diagonal = n * (n - 1) / 2)
            - SC: O(1)

        [Approach]
            clockwise rotation을 in-place로 하려면 다음의 순서로 수행한다.
                1. matrix reverse (by row)
                2. matrix transpose (diagonal)
        """

        n = len(matrix)

        # 1. matrix reverse (by row)
        for r in range(n // 2):
            matrix[r], matrix[n - r - 1] = matrix[n - r - 1], matrix[r]

        # 2. matrix transpose (diagonal)
        for r in range(n):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
