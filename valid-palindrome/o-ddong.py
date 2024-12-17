import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_phrase = re.sub("[^a-zA-Z0-9]", "", s).lower()

        if filtered_phrase == filtered_phrase[::-1]:
            return True
        else:
            return False
