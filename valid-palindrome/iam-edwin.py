class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < len(s) - 1 and not s[left].isalnum():
                left += 1
            while right > 0 and not s[right].isalnum():
                right -= 1

            if left >= right:
                return True
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True
