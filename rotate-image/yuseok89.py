# TC: O(N^2)
# SC: O(1)
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for k in range(0, n // 2):

            y11, x11 = k, k
            y12, x12 = k, n - 1 - k
            y21, x21 = n - 1 - k, k
            y22, x22 = n - 1 - k, n - 1 - k

            for _ in range(0, n - 1 - k * 2):
                matrix[y11][x11], matrix[y21][x21], matrix[y22][x22], matrix[y12][x12] = matrix[y21][x21], matrix[y22][x22], matrix[y12][x12], matrix[y11][x11]

                x11 += 1
                y12 += 1
                x22 -= 1
                y21 -= 1

