class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def dfs(k: int) -> bool:
            if k == len(s):
                return True
            for word in wordDict:
                if s[k : k + len(word)] == word:
                    if dfs(k + len(word)):
                        return True
            return False
        
        return dfs(0)
