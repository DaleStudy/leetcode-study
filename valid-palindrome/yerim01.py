# Goal: Return true if it's a palindrome. If it's not, return false
# - palindrome: a string that reads the same forward and backward
# Time Complexity: O(n)
# - Building string is O(n) + Two pointer check is O(n).
# Space Complexity: O(n)
# - We use a new string of size s.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        # Trim 's' to contain only alphanumerical characters
        for ch in s:
            if ch.isalnum():
                chars.append(ch.lower()) # make it case-insensitive

        new_s = "".join(chars)

        # Use two pointers
        # ptr1 -> starting index ptr2 -> ending index
        ptr1 = 0
        ptr2 = len(new_s) - 1

        while ptr1 < ptr2: # O(n) time
            # Return false if ptr1 and ptr2 point to different char
            if new_s[ptr1] != new_s[ptr2]:
                return False
            ptr1 += 1
            ptr2 -= 1

        # Otherwise, return true
        return True
