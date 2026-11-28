"""
https://leetcode.com/problems/number-of-1-bits/description/

시간 복잡도 : O(log n)
공간 복잡도 : O(1)
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            cnt += n % 2
            n //= 2
        return cnt
