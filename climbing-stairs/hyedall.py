"""
# http://leetcode.com/problems/climbing-stairs/description/

시간 복잡도 : O(n)
공간 복잡도 : O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n 

        prev2, prev1 = 1, 2

        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2, prev1 = prev1, current

        return current
