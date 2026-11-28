"""
n = s의 길이
시간 복잡도: O(n) - strip O(n) + 문자 거르기 반복문 O(n) + 앞뒤 비교 반복문 O(n)
공간 복잡도: O(n) - strip이 만든 복사본과 rm_s에 각각 최대 n글자씩 들어감
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s.strip():
            return True

        rm_s = []
        for i in range(len(s)):
            if '0' <= s[i] <= '9' or 'A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'z':
                if 'A' <= s[i] <= 'Z':
                    rm_s.append(s[i].lower())
                    continue
                rm_s.append(s[i])
            else:
                continue
        for i in reversed(range(len(rm_s))):
            if rm_s[i] != rm_s[len(rm_s) - 1 - i]:
                return False
        return True
