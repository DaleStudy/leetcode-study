"""
시간 복잡도: O(N)
공간 복잡도: O(N)

코드 가독성 개선 코드:
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_counter = Counter(s)
        t_counter = Counter(t)

        for num, freq in t_counter.items():
            if s_counter[num] != freq:
                return False
        
        return True
