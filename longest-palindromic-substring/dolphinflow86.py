# N is the length of the string s.
# TC: O(N^2) - expanding around each of the 2N - 1 possible centers takes up to O(N)
# SC: O(1) - constant auxiliary space tracking the start index and maximum length


class Solution:

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        start, max_len = 0, 0

        def expand(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1

        for i in range(len(s)):
            # Odd length palindrome (center is i)
            l1, len1 = expand(i, i)
            if len1 > max_len:
                start, max_len = l1, len1

            # Even length palindrome (center is between i and i + 1)
            l2, len2 = expand(i, i + 1)
            if len2 > max_len:
                start, max_len = l2, len2

        return s[start:start + max_len]
