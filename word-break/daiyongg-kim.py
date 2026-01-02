
""" Failed Attempt
 class Solution:
     def wordBreak(self, s: str, wordDict: List[str]) -> bool:

         for word in wordDict:
             if word in s:
                 s = s.replace(word, '')
             else:
                 return False
         return len(s) == 0
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]
