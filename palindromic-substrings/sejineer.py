"""
시간 복잡도: O(N^2)
공간 복잡도: O(1)
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        def count_palindrome(left: int, right: int):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        for i in range(len(s)):
            result += count_palindrome(i, i)
            result += count_palindrome(i, i + 1)
        return result
