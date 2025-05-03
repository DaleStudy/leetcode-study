"""
Time complexity O(n*m) n: len(s), m:len(wordDict)
Space compexity O(n)

dynamic programming
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s))]
        for i in range(len(s)):
            flag = False
            for word in wordDict:
                n = len(word)
                if i - n + 1 < 0:
                    continue
                if s[i-n+1:i+1] != word:
                    continue
                if i - n + 1 == 0:
                    flag = True
                    break
                elif i - n + 1 > 0:
                    if dp[i - n]:
                        flag = True
                        break
            dp[i] = flag
        return dp[-1]
