# TC : O(s^2*w)
# SC : O(s)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for n in range(1, len(s) + 1):
            for word in wordDict:
                if s[n - len(word) : n] == word:
                    dp[n] = dp[n - len(word)]
                if dp[n]:
                    break
        return dp[-1]
