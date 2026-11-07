"""
시간복잡도: O(n^2)
공간복잡도: O(1)

각 인덱스를 중심으로 팰린드롬을 확장하며 탐색
확장 함수로 팰린드롬의 좌우 경계 반환
가장 긴 팰린드롬 구간을 기록
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_left = best_right = 0

        def expand(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        for center in range(len(s)):
            for left, right in (
                expand(center, center),
                expand(center, center + 1),
            ):
                if right - left > best_right - best_left:
                    best_left, best_right = left, right

        return s[best_left : best_right + 1]
