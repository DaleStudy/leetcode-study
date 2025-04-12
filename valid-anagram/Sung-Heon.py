class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        try:
            for i in s:
                if len(t) == 0:
                    return False
                t.remove(i)
        except:
            return False
        if len(t) == 0:
            return True
        else:
            return False
