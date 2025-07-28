from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        # return Counter(s) == Counter(t)

        # str에서 제공하는 count 함수 활용
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True


