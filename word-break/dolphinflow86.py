# 1) I couldn't figure it out by myself this time, so I looked into the solution and found the DP approach. Key point here is that when an element of dp is True, use it as a checkpoint to slice the rest of the string.
# TC: O(N^3) where N is len(s)
# SC: O(N + L) where N is len(s), L is total length of characters in wordDict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        s_len = len(s)
        dp = [False] * (s_len + 1)
        dp[0] = True

        for i in range(1, s_len + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
        
        return dp[-1]
