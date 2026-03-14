class Solution:
    def climbStairs(self, n: int) -> int:
        # ways(n) = ways(n-1) + ways(n-2)

        if n == 1:
            return 1
        elif n == 2:
            return 2

        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2

        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n]

# Time Complexity: O(n)
# Space Complexity: O(n)
