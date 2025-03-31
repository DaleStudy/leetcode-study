'''
시간 복잡도: O(n^2)
공간 복잡도: O(1)
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_length = 0, 1  # Track longest palindrome

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return length of palindrome
            return right - left - 1
        
        # Check each position as potential center
        for i in range(len(s)):
            # Check for odd length palindromes (single character center)
            len1 = expand_around_center(i, i)
            # Check for even length palindromes (between two characters)
            len2 = expand_around_center(i, i + 1)
            
            curr_max = max(len1, len2)
            
            # Update start and max_length if current palindrome is longer
            if curr_max > max_length:
                max_length = curr_max
                start = i - (curr_max - 1) // 2
        
        return s[start:start + max_length]
