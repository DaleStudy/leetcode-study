"""
# Intuition
wordDict를 word들의 길이로 분류하고,
s의 각 위치까지의 문자열을 완성할 수 있는지 dp 배열로 확인합니다.

# Complexity
wordDict의 길이를 N, s의 길이를 K
- Time complexity: O(N+K)
- Space complexity: O(N+K)
"""

from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        word_dict = defaultdict(set)
        for word in wordDict:
            word_dict[len(word)].add(word)

        dp[0] = True
        for i in range(1, n + 1):
            for (
                k,
                v,
            ) in word_dict.items():
                if i + k - 1 > n:
                    continue
                if dp[i - 1] == False:
                    continue
                if s[i - 1 : i + k - 1] in v:
                    dp[i + k - 1] = True
        return dp[n]
