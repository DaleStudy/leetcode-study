# Palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring non-alphanumeric characters - letters and number).
# the solution should first filter out non-alphanumeric characters and convert the string to lowercase.
# Then, it should check if the cleaned string is equal to its reverse.

# Time complexity = O(n), as it checks, replaces, converts to lowercase, and reverses all characters in the string
# Space complexity = O(n), as it creates a new string with a maximum length equal to the original string
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        reversed_string = filtered_string[::-1]
        return reversed_string == filtered_string
