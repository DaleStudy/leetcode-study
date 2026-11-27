"""
TC: O(N) - 문자열을 한 번 순회
SC: O(N) - N + 1 크기의 DP 배열 사용
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[n]
