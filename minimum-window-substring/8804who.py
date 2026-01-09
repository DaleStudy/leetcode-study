from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer = ''
        counter = Counter(t)
        now = defaultdict()

        start = 0
        end = 0
        
        now[s[start]] = 1

        while start<=end and end < len(s):
            enough = True
            for key in counter.keys():
                if key not in now or now[key] < counter[key]:
                    enough = False
        
            if enough:
                if answer == '' or len(answer) > end-start+1:
                    answer = s[start:end+1]

                now[s[start]] -= 1
                start += 1
            else:
                end += 1
                if end == len(s):
                    break
                if s[end] not in now:
                    now[s[end]] = 0
                now[s[end]] += 1
        
        return answer
    
