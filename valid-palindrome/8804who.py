import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed_string = re.sub('[^a-zA-Z0-9]','',s).upper()
        return parsed_string == parsed_string[::-1]
    
