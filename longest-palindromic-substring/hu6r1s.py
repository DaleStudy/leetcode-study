class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s) <= 2:
        #     return s[0]

        # for i in range(2, len(s)):
        #     for k in range(len(s)-i):
        #         if s[k:k+i] == s[k:k+i][::-1]:
        #             return s[k:k+i]

        max_s, max_e = 0, 0

        for i in range(len(s)):
            start, end = i, i
            while 0 <= start and end < len(s) and s[start] == s[end]:
                if max_e - max_s < end - start:
                    max_s, max_e = start, end
                start, end = start - 1, end + 1

            start, end = i, i + 1
            while 0 <= start and end < len(s) and s[start] == s[end]:
                if max_e - max_s < end - start:
                    max_s, max_e = start, end
                start, end = start - 1, end + 1

        return s[max_s : max_e + 1]
