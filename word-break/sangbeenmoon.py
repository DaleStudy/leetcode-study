# 실패한 풀이.
# AC 를 받기는 했으나 test case 가 좀 더 촘촘했다면 TLE 에 걸렸을 것임.
# string 이 아닌 index 로 memoization 을 하는 걸 떠올려보자.

class Solution:
    answer = False
    visited = {}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        self.answer = False
        self.visited = {}
        self.go(0,s,wordDict)

        return self.answer

    def go(self, i:int, s: str, wordDict: List[str]):
        if i >= (len(s)):
            self.answer = True
            return
        
        for word in wordDict:
            if i + len(word) > len(s):
                continue

            if word == s[i:i + len(word)]:
                if not s[i + len(word) : ] in self.visited:
                    self.go(i + len(word), s, wordDict)
        
        self.visited[s[i:]] = False







# -----------
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        visited = {}
        dp = [True] * len(s)
        for word in wordDict:
            visited[word] = True
                
        def go(start: int) -> bool:
            if start >= len(s):
                return True
            
            if not dp[start]:
                return False
            
            for end in range(start + 1, len(s) + 1):
                target = s[start:end]
                
                if target in visited:
                    if go(end):
                        return True
            
            dp[start] = False
            return False
    
        return go(0)
