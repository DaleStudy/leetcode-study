# m is the length of text1 and n is the length of text2
# TC : O(m * n)
# SC : O(m * n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for r in range(1, len(text1) + 1):
            for c in range(1, len(text2) + 1):
                if text1[r - 1] == text2[c - 1]:
                    dp[r][c] = 1 + dp[r - 1][c - 1]
                else:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
        return dp[-1][-1]
