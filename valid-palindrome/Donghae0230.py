# 시간복잡도 O(n): reversed 함수 사용
# 공간복잡도 O(n): cleaned_s, reversed_s 사용
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        reversed_s = ''.join(reversed(cleaned_s))
        if cleaned_s == reversed_s:
            return True
        else:
            return False
