class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = 65
        answer = 1
        for i in range(26):
            t = chr(n+i)
            start = 0
            end = 0
            x = 1 if s[start] != t else 0

            while True:
                if x > k:
                    if s[start] != t:
                        x -= 1
                    start += 1
                else:
                    end += 1
                    if end == len(s):
                        break
                    if s[end] != t:
                        x += 1
                if x <= k:
                    answer = max(answer, end-start+1)
        return answer
                
    
