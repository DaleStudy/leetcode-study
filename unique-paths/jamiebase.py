"""
# Approach
(0,0) -> (m-1, n-1)로 가기 위해서는 아래로는 m-1회, 우측으로 n-1회 이동해야 합니다.
도합 m+n-2회 이동해야 합니다. 그 이동 경로 중에서 방향 전환(우측 이동 혹은 아래쪽 이동)을 하는 경우의 수를 계산하여 unique path를 구합니다.

# Complexity
- Time complexity: math.comb는 거의 상수 시간으로 취급하므로 O(1)
- Space complexity: O(1)
"""

import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)
