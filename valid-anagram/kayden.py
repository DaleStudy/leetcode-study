# 시간복잡도: O(N)
# 공간복잡도: O(N)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = {}
        for letter in s:
            counter_s[letter] = counter_s.get(letter, 0) + 1

        counter_t = {}
        for letter in t:
            counter_t[letter] = counter_t.get(letter, 0) + 1

        for letter, cnt in counter_s.items():
            if counter_t.get(letter, 0) != cnt:
                return False

        return True
