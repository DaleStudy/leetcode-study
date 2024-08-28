"""
    TC: O(n^2)

    TC in first try was O(n^3).
    It is the improved codes from neetcodes
    key point is that each character in loop is considered to middle one.
    Ant then, check left end and right end.

"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += self.countPalindrom(s, i, i)
            result += self.countPalindrom(s, i, i+1)
        return result


    def countPalindrom(self, s, left_end, right_end):
        result = 0
        while left_end >= 0 and right_end < len(s) and s[left_end] == s[right_end]:
            result += 1
            left_end -= 1
            right_end += 1

        return result
