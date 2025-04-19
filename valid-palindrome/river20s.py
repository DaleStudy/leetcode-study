import re

class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        return s == s[::-1]
