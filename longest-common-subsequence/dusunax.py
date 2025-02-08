'''
# 1143. Longest Common Subsequence

use DP table.

> key: tuple(current index in text1, current index in text2)
> value: LCS of text1[i:] and text2[j:]
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def helper(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + helper(i + 1, j + 1)
            else:
                dp[(i, j)] = max(helper(i + 1, j), helper(i, j + 1))

            return dp[(i, j)]

        return helper(0, 0)
