from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = start = end = 0
        for right, char in enumerate(s):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            while missing == 0:
                if end == 0 or right - left < end - start:
                    start, end = left, right + 1
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        return s[start:end]
    