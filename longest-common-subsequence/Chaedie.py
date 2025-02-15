"""
Solution: 재귀를 활용한 풀이, memo 를 활용한 시간복잡도 개선

Time: O(m * n)
Space: O(2 * m * n)
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(text1) or j == len(text2):
                memo[(i, j)] = 0
            elif text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return memo[(i, j)]

        return dfs(0, 0)
