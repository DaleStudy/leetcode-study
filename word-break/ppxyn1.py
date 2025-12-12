# idea: recursive 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # TLE > (solution : memorization with @cache decoration)
        # @cache : If a function is called more than once with the same arguments, it uses stored memoization results instead of recomputing.
        def dfs(start):
            if start == len(s):
                return True
            for word in wordDict:
                if s[start:start+len(word)] == word:
                    if dfs(start+len(word)):
                        return True
            return False
        return dfs(0)

    


