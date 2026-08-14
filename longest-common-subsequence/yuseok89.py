# TC: O(N*M)
# SC: O(M)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(m + 1)] for _ in range(2)]

        cur, prev = 1, 0

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[cur][j + 1] = dp[prev][j] + 1
                else:
                    dp[cur][j + 1] = max(dp[prev][j + 1], dp[cur][j])

            cur, prev = prev, cur

        return dp[prev][m]

