"""
        문제 요약
        - 32비트 부호 없는 정수 n의 이진 표현에서 '1'의 개수(= set bits)를 구하라.

        아이디어 A: 브라이언 커니핸(Brian Kernighan) 알고리즘
        - 핵심 관찰: n & (n - 1)은 n의 최하위 1비트를 '0'으로 만든다.
        예) n = 0b101100 → n-1 = 0b101011 → n & (n-1) = 0b101000 (최하위 1 하나 삭제)
        - 따라서 '1'의 개수만큼 루프가 돈다.
        - 시간복잡도: O(k)  (k = n의 1비트 개수)  ← 매우 빠름
        - 공간복잡도: O(1)
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= n - 1   # 최하위 1비트 제거
            cnt += 1
        return cnt
