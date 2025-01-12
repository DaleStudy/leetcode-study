# O(2^s*w) times, O(s) space
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dfs(start):
            if start == len(s):
                return True
            for word in wordDict:
                if s[start:start+len(word)] == word:
                    if dfs(start+len(word)):
                        return True
            return False
        
        return dfs(0)
