class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        len_res = 0
        len_s = len(s)

        for i in range(len_s):
            left, right = i, i
            while 0 <= left and right < len_s:
                if s[left] == s[right]:
                    if right - left + 1 > len_res:
                        res = s[left:right + 1]
                        len_res = right - left + 1
                    left -= 1
                    right += 1
                else:
                    break

        for i in range(len_s - 1):
            left, right = i, i + 1
            while 0 <= left and right < len_s:
                if s[left] == s[right]:
                    if right - left + 1 > len_res:
                        res = s[left:right + 1]
                        len_res = right - left + 1
                    left -= 1
                    right += 1
                else:
                    break

        return res
