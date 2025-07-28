class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = list(s)
        for d in t:
            if d in s and d in l:
                l.remove(d)
            else:
                return False

        if not l:
            return True
        else:
            return False
        