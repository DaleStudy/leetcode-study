class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            dist = 0
            temp = ""
            while i-dist >= 0 and i+dist < len(s):
                if s[i-dist] == s[i+dist]:
                    temp = s[i-dist:i+dist+1]
                    dist+=1
                else:
                    break
            if len(temp) > len(answer):
                answer = temp
            if i+1 < len(s):
                if s[i] != s[i+1]:
                    continue
                dist = 0
                while i-dist >= 0 and i+1+dist < len(s):
                    if s[i-dist] == s[i+1+dist]:
                        temp = s[i-dist:i+dist+2]
                        dist+=1
                    else:
                        break
            if len(temp) > len(answer):
                answer = temp
        return answer
    
