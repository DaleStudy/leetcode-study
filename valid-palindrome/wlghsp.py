"""
N: 문자열 s의 길이

TC : O(N)
- 투포인터(left, right)가 이동하며 각 문자를 최대 상수 번 검사

SC: O(1)
- 입력 크기와 관계 없이 두 개의 포인터만 사용
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
