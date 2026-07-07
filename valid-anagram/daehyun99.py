from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        if len(s) != len(t):
            return False

        for s_, t_ in zip(s, t):
            count[s_] += 1
            count[t_] -= 1
        
        for key, val in count.items():
            if val != 0:
                return False
        return True
