# 1) Iterate through the string using two-pointers, skipping non-alphanumeric characters and comparing them in lowercase to validate the palindrome in-place.
# TC: O(N) where N is the length of s
# SC: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower(): return False
            left += 1
            right -= 1 
    
        return True

# 2) Filter alphanumeric characters and conver them to lowercase to create a new string and then simply validate palindrome using two-pointers
# TC: O(N) where N is the length of s
# SC: O(N) where N is the length of s
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for ch in s:
            if ch.isalnum():
                new_str += ch.lower()

        n = len(new_str)
        left = 0
        right = n - 1

        while left < right:
            if new_str[left] != new_str[right]: return False
            left += 1
            right -= 1 

        return True
