# idea : palindrome
# Time Complexity: O(n^2)

class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        
        for i in range(len(s)):            
            # odd 
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
            
            # even
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
        
        return result



