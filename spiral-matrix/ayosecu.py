from typing import List

class Solution:
    """
        - Time Complexity: O(N), N = len(matrix) * len(matrix[0])
        - Space Complexity: O(1), If output variable (result) excluded.
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            result += matrix.pop(0)             # append a top row
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())    # append elements in right side (down direction)
            if matrix:
                result += matrix.pop()[::-1]    # append a bottom row with reversed
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))   # append elements in left side (up direction)

        return result

tc = [
        ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7])
]

sol = Solution()
for i, (m, e) in enumerate(tc, 1):
    r = sol.spiralOrder(m)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
