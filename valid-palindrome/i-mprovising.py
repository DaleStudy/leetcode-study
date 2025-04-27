"""
Time complexity O(n)
Space complexity O(n)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # preprocessing
        string = [c for c in s.lower() if c.isalnum()]

        if string == [c for c in string[::-1]]:
            return True
        return False
