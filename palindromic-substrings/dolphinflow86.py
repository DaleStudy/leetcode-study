# N is the length of string s.
# TC: O(N^2) - expands around each center (2N - 1 possible centers)
# SC: O(1) - uses only constant extra space
class Solution:

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        sub_count = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            sub_count += 1
            left -= 1
            right += 1

        return sub_count

    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            count += self.expand_around_center(s, i, i)
            count += self.expand_around_center(s, i, i + 1)

        return count
