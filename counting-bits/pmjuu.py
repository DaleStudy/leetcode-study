'''
시간 복잡도: O(n)
공간 복잡도: O(n)
'''
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp
