"""
Title: 215. Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/  

Summary:
    - Palindrome이라면 True, 아니라면 False를 반환하는 문제.
    - Palindrome이란, 대문자를 소문자로 변환하고 알파벳과 숫자 이외의 문자를 제거한 후에도 
      앞으로 읽어도 뒤에서부터 읽어도 동일한 단어를 뜻함.
    - e.g. racecar

Conditions:
    - 입력 문자열이 Palindrome인 경우: `True` 반환
    - Palindrome이 아닌 경우: `False` 반환

Time Complexity:
    - O(n)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-z]', '', s).lower()
        if s == s[::-1]:
            return True
        return False
