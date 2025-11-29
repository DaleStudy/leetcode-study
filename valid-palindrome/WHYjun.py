class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]

        if len(s) == 1:
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
