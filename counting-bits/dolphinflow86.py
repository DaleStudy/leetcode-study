# N is the given integer.
# TC: O(N) - single pass from 0 to N using previous subproblem results
# SC: O(1) - auxiliary space (O(N) to store the result array)

from typing import List


class Solution:

    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
