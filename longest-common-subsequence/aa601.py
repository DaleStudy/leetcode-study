'''
TC : O(nm)
SC : O(nm)
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #dp 2차원 배열 생성
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        #i와 j는 dp기준
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[i][j]
