"""
Blind75 - Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

시간복잡도 O(n), 공간복잡도 O(n)

isalnum() 함수는 시간복잡도 O(1)이므로 필터링하는 과정도 O(n)이다.
[::-1] 슬라이싱도 O(n)이다.
따라서 전체 시간복잡도는 O(n)이다.


Runtime   Beats
7ms       82.67%

Memory    Beats
23.14 MB  17.23%
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ''.join(char.lower() for char in s if char.isalnum())
        return filtered_s == filtered_s[::-1]
    
