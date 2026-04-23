class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        last_seen = {}
        answer = 0

        for i,ch in enumerate(s):
            if ch in last_seen:
                if start < last_seen[ch]:
                    start = last_seen[ch] + 1

            last_seen[ch] = i
            answer = max(answer, i - start + 1)
            
        return answer
