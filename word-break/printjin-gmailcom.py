class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}
        
        def backtrack(start):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet and backtrack(end):
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False
        
        return backtrack(0)
