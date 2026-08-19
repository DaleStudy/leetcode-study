class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        # odd
        for i in range(0, len(s)):
            m, n = i, i
            while 0 <= m and n < len(s) and s[m] == s[n]:
                result += 1
                m -= 1
                n += 1

        # even
        for i in range(0, len(s)-1):
            m, n = i, i+1
            while 0 <= m and n < len(s) and s[m] == s[n]:
                result += 1
                m -= 1
                n += 1
        return result



