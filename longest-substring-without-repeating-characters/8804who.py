class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        answer = 0
        character_set = set()
        while end<len(s):
            while s[end] in character_set:
                character_set.remove(s[start])
                start += 1
            character_set.add(s[end])
            if answer < end-start+1:
                answer = end-start+1
            end += 1
        return answer
    
