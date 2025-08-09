# isalnum() : 문자열이 영어, 한글 숫자 -> True , 아니라면 False
class Solution:
    def isPalindrome(self, s: str) -> bool:
        changed_s = [c.lower() for c in s if c.isalnum()]
        return changed_s == changed_s[::-1]
