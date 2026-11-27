# TC: O(n), 문자열을 순회하며 조작
# SC: O(n), 문자열의 길이만큼 새로운 문자열 할당
# 풀이
# 1. 정규식을 활용하여 알파벳과 숫자만 남기고 같은 문자열인지 비교
# 2. two pointer를 활용하여 팰린드롬 체크
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left, right = 0, len(alphanumeric_s) - 1

        while left < right:
            if alphanumeric_s[left] != alphanumeric_s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True

