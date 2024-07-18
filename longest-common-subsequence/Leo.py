class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)

        for i in range(len(text1)):
            prev_row = dp[:]
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[j + 1] = prev_row[j] + 1
                else:
                    dp[j + 1] = max(dp[j], prev_row[j + 1])

        return dp[-1]

        ## TC: O(mn), SC: O(n)
