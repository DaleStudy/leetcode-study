"""
48. Rotate Image
https://leetcode.com/problems/rotate-image/

Solution:
    To solve this problem, we can follow the following steps:
    1. Process layers from the outermost to the innermost.
    2. For each layer, iterate through the elements in the layer.
    3. Swap the elements in the layer in a clockwise direction.
    4. Repeat the process for all layers.

Time Complexity: O(n^2)
    - We need to process all elements in the matrix.
    - The time complexity is O(n^2).

Space Complexity: O(1)
    - We are rotating the matrix in place without using any extra space.
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Process layers from the outermost to the innermost
        for layer in range(n // 2):
            first = layer
            last = n - layer - 1
            for i in range(first, last):
                offset = i - first
                # Save the top element
                top = matrix[first][i]

                # Move left element to top
                matrix[first][i] = matrix[last - offset][first]

                # Move bottom element to left
                matrix[last - offset][first] = matrix[last][last - offset]

                # Move right element to bottom
                matrix[last][last - offset] = matrix[i][last]

                # Assign top element to right
                matrix[i][last] = top
