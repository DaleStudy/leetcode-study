class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        start, max_length = 0, 1

        for i in range(1, len(s)):
            odd_s = i - max_length - 1
            even_s = i - max_length
            odd_p = s[odd_s:i + 1]
            even_p = s[even_s:i + 1]

            if odd_s >= 0 and odd_p == odd_p[::-1]:
                start = odd_s
                max_length += 2
            elif even_p == even_p[::-1]:
                start = even_s
                max_length += 1

        return s[start:start + max_length]

        ## TC: O(n^2), SC: O(1)
