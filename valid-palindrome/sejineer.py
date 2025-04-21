"""
시간 복잡도: O(N)
공간 복잡도: O(N)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filterd_s = [ch for ch in s.lower() if ch.isalnum()]
        return filterd_s == filterd_s[::-1]
