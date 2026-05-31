class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # for i in range(len(s)):
        #     if sorted_s[i] != sorted_t[i]:
        #         return False
        # return True
        # 시간복잡도가 O(nlog(n))

        # Hashmap 사용하는 방법으로 변경
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        for char in t:
            if char in counter and counter[char] != 0:
                counter[char] -= 1
            elif char in counter and counter[char] == 0:
                return False
            else:
                return False
        # 시간복잡도 O(n)
        # 공간복잡도 O(n)
        return True
