import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        replaced_string = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        if len(replaced_string) == 0:
            return True

        start, end = 0, len(replaced_string)-1

        while start <= len(replaced_string) // 2:
            if replaced_string[start] is not replaced_string[end]:
                return False
            
            start += 1
            end -= 1
        
        return True
