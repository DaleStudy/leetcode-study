"""
# Approach
양 끝에 포인터를 두고 파이썬의 isalnum(), lower() 문자열 메소드로 검사합니다.

# Complexity
- Time complexity: s의 길이를 N이라고 할 때, O(N)

- Space complexity: O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
