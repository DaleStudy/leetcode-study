class Solution:
    def isAlphaNum(self, c : str):
        return 'a' <= c.lower() <= 'z' or '0' <= c <= '9'
    
    # Time complexity: O(n)
    # Space complexity: O(1)
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right: 
            if self.isAlphaNum(s[left]) and self.isAlphaNum(s[right]):
                if s[left].lower() != s[right].lower():
                    return False 
                left, right = left + 1, right - 1
            else:
                left, right = left + (not self.isAlphaNum(s[left])), right - (not self.isAlphaNum(s[right]))
    
        return True