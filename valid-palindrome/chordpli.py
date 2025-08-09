import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        lower_eng_str = re.sub(r"[^a-z0-9]", "", lower_s)
        reverse_str = lower_eng_str[::-1]

        if lower_eng_str == reverse_str:
            return True

        return False