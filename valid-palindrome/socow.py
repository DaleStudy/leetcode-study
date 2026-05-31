"""
        문제 요약
        - 영숫자만 고려, 대소문자 무시 → 팰린드롬 여부

        아이디어
        - 소문자 변환 → 영숫자만 필터 → 역순과 동일한지 비교

        시간복잡도: O(n)
        공간복잡도: O(n)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c for c in s.lower() if c.isalnum()]
        return cleaned == cleaned[::-1]
