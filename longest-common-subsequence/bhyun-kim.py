"""
1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence

Solution:
    To solve this problem, we can use the dynamic programming approach.
    We create a 2D list to store the length of the longest common subsequence of the two strings.
    We iterate through the two strings and update the length of the longest common subsequence.
    We return the length of the longest common subsequence.

Time complexity: O(n1 * n2)
    - We iterate through each character in the two strings once.
    - The time complexity is O(n1 * n2) for updating the length of the longest common subsequence.

Space complexity: O(n1 * n2)
    - We use a 2D list to store the length of the longest common subsequence of the two strings.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0 for i in range(n2 + 1)] for j in range(n1 + 1)]
        maximum = 0
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            maximum = max(dp[i][j], maximum)

        return maximum
