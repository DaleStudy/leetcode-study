"""
338. Counting Bits
https://leetcode.com/problems/counting-bits/

Solution:
    DP를 활용한 풀이
    - i의 1비트 개수 = (i // 2)의 1비트 개수 + (i % 2)
    - i // 2는 i를 오른쪽으로 1비트 shift한 것 (이미 계산된 값)
    - i % 2는 LSB(최하위 비트)가 1인지 여부

    예시: 5 = 101(2)
    - 5 // 2 = 2 = 10(2) → 1비트 1개
    - 5 % 2 = 1 → LSB가 1
    - 따라서 5의 1비트 개수 = 1 + 1 = 2

Time: O(n)
Space: O(1) - 결과 배열 제외
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp
