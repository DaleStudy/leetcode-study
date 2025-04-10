class Solution:
    # time complexity: O(n)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
    
        prev1, prev2 = 1, 2
        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current
        return prev2
