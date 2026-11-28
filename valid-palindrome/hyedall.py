"""
https://leetcode.com/problems/valid-palindrome/description/

시간 복잡도 : O(n)
공간 복잡도 : O(n)
"""

import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)

        for i in range(len(s) // 2):
            if s[i] != s [-i - 1]:
                return False
        return True
