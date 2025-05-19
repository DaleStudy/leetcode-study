from collections import deque

class Solution:
    """
    Time complexity O(n)
    Space complexity O(n)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        q = deque()
        for i, ch in enumerate(s):
            if ch not in q:
                q.append(ch)
                if len(q) > max_len:
                    max_len = len(q)
            else:
                while True:
                    tmp = q.popleft()
                    if tmp == ch:
                        break
                q.append(ch)
    
        return max_len
    
    def slidingWindow(self, s):
        start, end = 0, 0
        substr = set()
        max_len = 0
        while end < len(s):
            if s[end] in substr:
                substr.remove(s[start])
                start += 1
            else:
                substr.add(s[end])
                end += 1
                max_len = max(end - start, max_len)
        return max_len
