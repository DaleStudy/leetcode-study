"""
O(n) complexity
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        phrase = [c.lower() for c in s if c.isalpha() or c.isdigit()]

        if phrase == phrase[::-1]:
            return True
        return False
        
        