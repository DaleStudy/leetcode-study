class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand_and_get_length(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        for i in range(len(s)):
            odd_palindrome_length = expand_and_get_length(s, i, i)
            even_palindrome_length = expand_and_get_length(s, i, i + 1)

            max_len = max(odd_palindrome_length, even_palindrome_length)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start : end + 1]
