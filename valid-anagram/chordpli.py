class Solution:
    # dictionary 사용 11ms
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}
        for char in s:
            if char not in check:
                check[char] = 0
            check[char] += 1
        for char in t:
            if char not in check:
                return False
            check[char] -= 1
            if check[char] == 0:
                del check[char]
        return not check

    # 정렬 사용 15 - 20ms
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(s) == sorted(t)
