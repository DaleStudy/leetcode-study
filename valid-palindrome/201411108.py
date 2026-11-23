# TC: O(n), 문자열을 순회하며 조작
# SC: O(n), 문자열의 길이만큼 새로운 문자열 할당
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        without_blank = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        alphanumeric_s = without_blank[::-1]

        return without_blank == alphanumeric_s

