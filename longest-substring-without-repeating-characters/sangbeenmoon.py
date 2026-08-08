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


# ------
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0

        answer = 0

        dictionary = {}

        for i,ch in enumerate(s):
            right += 1
            if ch not in dictionary:
                dictionary[ch] = i
            else:
                idx = dictionary[ch]
                if left <= idx:
                    left = idx + 1
                dictionary[ch] = i

            print(right, left)
            answer = max(answer, right - left)

        return answer
