class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if i - j < 0 or i + j >= len(s):
                    break
                if s[i-j] == s[i+j]:
                    answer += 1
                else:
                    break
            
            if i+1 >= len(s) or s[i] != s[i+1]:
                continue
            for j in range(len(s)):
                if i - j < 0 or i + 1 + j >= len(s):
                    break
                if s[i-j] == s[i+1+j]:
                    answer += 1
                else:
                    break
        return answer
    
