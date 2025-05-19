"""
시간 복잡도: O(N)
공간 복잡도: O(N) 
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        start, end = 0, 0

        result = 0

        while end < len(s):
            if s[end] in s_set:
                s_set.remove(s[start])
                start += 1
            else:
                s_set.add(s[end])
                end += 1
                result = max(result, end - start)
        
        return result
