# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        """
        [Complexity]
            - TC: O(nlogn)
            - SC: O(n)
        """
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)
        """
        from collections import Counter

        return Counter(s) == Counter(t)

    def isAnagram(self, s: str, t: str) -> bool:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)
        """
        from collections import defaultdict

        cnt = defaultdict(int)

        for _s in s:
            cnt[_s] += 1
        for _t in t:
            cnt[_t] -= 1

        for k, v in cnt.items():
            if v != 0:
                return False

        return True
