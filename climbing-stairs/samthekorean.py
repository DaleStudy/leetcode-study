# Time complexity : O(n)
# Space complexity : O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        result = 0
        if n == 1:
            return a

        if n == 2:
            return b

        for i in range(3, n + 1):
            result = a + b
            a, b = b, result

        return result
