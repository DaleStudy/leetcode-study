import re


class Solution:
    # Time: O(n)
    # Space: O(1)
    def isPalindrome(self, s: str) -> bool:
        # 1. Convert string
        # Time: O(n)
        # Space: O(n) since re.sub() will internally use a new string of length n.
        s = re.sub('[^a-z0-9]', '', s.lower())
        length = len(s)
        # 2. Check if the string reads the same forward and backward, one by one.
        # Time: O(n)
        # Space: O(1)
        for i in range(length):
            if (s[i] != s[length - 1 - i]):
                return False
        return True
