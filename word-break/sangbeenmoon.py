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
