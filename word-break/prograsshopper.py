# Time complexity: O(N∗N∗M)
# Space complexity: O(N)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordSet = set(wordDict)

        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j]:
                    if s[j:i] in wordSet:
                        dp[i] = True
                        break
        return dp[len(s)]
