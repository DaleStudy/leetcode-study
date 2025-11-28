class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = [char for char in s if char.isalnum()]

        n = len(result)
        for i in range(n):
            str1 = result[i]
            if (str1 != result[n-i-1]):
                return False
        return True
    
    