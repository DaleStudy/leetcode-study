
import re

class Solution:
# Palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring non-alphanumeric characters - letters and number).
# the solution should first filter out non-alphanumeric characters and convert the string to lowercase.
# Then, it should check if the cleaned string is equal to its reverse.

# Time complexity = O(n), as it checks, replaces, converts to lowercase, and reverses all characters in the string
# Space complexity = O(n), as it creates a new string with a maximum length equal to the original string
    def isPalindrome(self, s: str) -> bool:
        filtered_string = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        reversed_string = filtered_string[::-1]
        return reversed_string == filtered_string


# Using Two-pointer; It searches from given string directly so the Space complexity is O(n) - better method
# By using two index, searchs and compares from start and end of the string like this -><- 
# Do this while start index is less than end index
# Skip non-alphanumeric characters
# If both pointer are in characters, then convert to lowercase and compare
# If not equal, return false
# If all characters are equal, return true

# Time complexity = O(n), as it checks and converts to lowercase all characters in the string
# Space complexity = O(1), as it uses only a constant amount of extra space
    def isPalindromeTwoPointer(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[left].lower() != s[right].lower():
                return False
            
            left+=1
            right-=1

        return True
