# 재배치하여 다른 문자를 만들 수 있는지 여부
# 시간복잡도 / 공간복잡도 O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

