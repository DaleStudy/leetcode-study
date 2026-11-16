# TC: O(n log n), sort 메서드가 O(n log n)이기 때문
# SC: O(n), 리스트의 길이가 n
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        list_s = list(s)
        list_t = list(t)
        
        list_s.sort()
        list_t.sort()

        for i in range(len(s)):
            if list_s[i] != list_t[i]:
                return False

        return True

