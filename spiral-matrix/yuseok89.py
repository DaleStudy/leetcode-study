# TC: O(N*M)
# SC: O(N*M)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        row, col, dir = 0, -1, 1

        n -= 1

        while n >= 0 and m >= 1:
            for i in range(0, m):
                col += dir
                ans.append(matrix[row][col])

            for i in range(0, n):
                row += dir
                ans.append(matrix[row][col])

            n -= 1
            m -= 1
            dir *= -1

        return ans;

