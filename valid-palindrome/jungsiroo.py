import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
		# Fastest - tc : O(n) / sc : O(1
        s = ''.join(re.findall(r'[a-z0-9]+', s.lower()))
        return s == ''.join(reversed(s))
