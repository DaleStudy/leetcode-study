class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer
        left, right = 0, len(s) - 1

        while left < right:
            # compare only alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # compare with lowercase
            if s[left].lower() != s[right].lower():
                return False
            
            # move pointers
            left += 1
            right -= 1
        
        return True
