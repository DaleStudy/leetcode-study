# Time: O(n + m) on average, Space: O(1)
# n = len(s), m = len(t); at most 26 distinct lowercase letters.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1

        count_t = {}
        for char in t:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1

        return count_s == count_t

