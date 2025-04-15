class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            a[s[i]] = a.get(s[i], 0) + 1
            b[t[i]] = b.get(t[i], 0) + 1

        return a == b
