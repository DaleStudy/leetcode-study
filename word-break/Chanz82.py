class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        visited = set()
        
        def dfs(start):
            if start == len(s):
                return True
            
            if start in visited:
                return False
            
            for word in wordDict:
                if s[start:start+len(word)] == word:
                    if dfs(start+len(word)):
                        return True
            
            visited.add(start)
            return False

        return dfs(0)
    
