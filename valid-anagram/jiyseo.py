class Solution(object):
    def isAnagram(self, s, t):
        # 시간복잡도 = O(N * (N + M))
        if len(s) != len(t) :
            return False

        for i in set(s) :
            if s.count(i) != t.count(i) :
                return False

        return True

