"""
첫번째 풀이
시간 복잡도 : O(n log n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

"""
두번째 풀이
시간 복잡도 : O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 반례 : s = ab, t = a
        # 이 경우에는 t에 없는 b가 존재하므로 False를 반환해야 한다.
        if len(s) != len(t):
            return False
        counter = {}

        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1

        for ch in t:
            if ch not in counter:
                return False
            counter[ch] -= 1
            if counter[ch] < 0:
                return False
        return True
