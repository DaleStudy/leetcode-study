## TC: O(n), SC:O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1

        for i in range(n - 1):
            a, b = a + b, a

        return a
