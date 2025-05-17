"""
시간 복잡도: O(n * D * L) n = 문자열 길이, D = 사전 크기, L = 단어 평균 길이
공간 복잡도: O(n)
"""
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
