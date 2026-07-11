class Solution:
    # dynamic programming with bottom-up
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        prev1, prev2 = 2, 1

        for i in range(3, n+1):
            prev1, prev2 = prev2 + prev1, prev1

        return prev1
