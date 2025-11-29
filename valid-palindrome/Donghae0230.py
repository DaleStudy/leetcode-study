# 문제 풀이
# 1. 문자열을 소문자로 변환 후 문자와 숫자가 아닌 값을 제거
# 2. 문자열을 뒤집은 후 원래 문자열과 비교

# 시간복잡도 O(n): 문자열 처리(re.sub, reversed 등) 사용
# 공간복잡도 O(n): 원래 문자열 만큼의 공간 사용
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        reversed_s = ''.join(reversed(cleaned_s))
        if cleaned_s == reversed_s:
            return True
        else:
            return False
