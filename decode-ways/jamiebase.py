"""
# Intuition
dp[n]은 s의 n번째 글자까지 디코딩할수 있는 경우의 수
dp[n] = dp[n-1](if can be decoded) + dp[n-2](if can be decoded)

# Approach
i-1 ~ i까지의 숫자, i-2 ~ i까지의 숫자가 각각 디코딩 될 수 있는지 확인한다.
디코딩 가능하면 그 위치의 dp 배열의 값을 각각 더하고, 디코딩 불가능하면 더하지 않는다.

# Complexity
- Time complexity: N을 s의 길이라고 할 때, 반복문으로 O(N)

- Space complexity: dp 배열 만드는 데에 O(N)
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[1] = 1 if s[0] != "0" else 0
        if dp[1] == 0 or n == 1:
            return dp[1]
        dp[2] = 1 if int(s[1]) > 0 else 0
        dp[2] += 1 if int(s[:2]) > 9 and int(s[:2]) < 27 else 0
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] if s[i - 1 : i] != "0" else 0
            dp[i] += dp[i - 2] if s[i - 2 : i] > "09" and s[i - 2 : i] < "27" else 0
        return dp[n]
