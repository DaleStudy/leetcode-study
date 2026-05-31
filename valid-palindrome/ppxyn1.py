# idea : regex
import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = re.sub(r'[^A-Za-z0-9]', '', s).lower()

        return alphabet == alphabet[::-1]

        

