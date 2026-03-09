# 125. Valid Palindrome 
# Solution 1: Can early return False if chars don't match, so O(1) space.
# Solution 2: Normalize the string first, then check if it's a palindrome. O(n) space for the normalized string.

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isPalindrome(self, s: str) -> bool:
        # Use two pointers from both ends
        left, right = 0, len(s) - 1

        # Move inward from both ends, ignore non-alphanumeric chars
        # and compare chars case-insensitively. 
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isPalindrome2(self, s:str) -> bool:
        # Normalize the string by keeping only lowercase alphanumeric characters
        s = list(filter(str.isalnum, s.lower()))
        
        # Check if the list is the same forwards and backwards 
        return s == s[::-1]
