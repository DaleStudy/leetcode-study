"""
# Intuition
마지막 계단에 도착하는 경우의 수는, 2스텝 전의 경우의 수와 1스텝 전의 경우의 수를 합한 값입니다.

# Approach
dp[n] = dp[n-1] + dp[n-2]

# Complexity
- Time complexity: O(n)

- Space complexity: O(1)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        b = 1  # n이 1일때
        if n == 1:
            return b
        a = 2  # n이 2일때
        if n == 2:
            return a

        for n in range(3, n + 1):  # O(n)
            a, b = a + b, a
        return a
