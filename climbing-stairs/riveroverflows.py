from typing import *


class Solution:
    """
    TC: O(n)
    - memo = [-1] * (n+1): O(n)
    - for num in range(3, n+1): O(n)
    최종: O(n)

    SC: O(n)
    - memo: O(n)

    풀이:
    n번째 계단까지 올라가는 방법의 수는 (n-1번째 방법의 수) + (n-2번째 방법의 수).
    피보나치수열과 동일한 점화식. memoization으로 중복 계산 방지.
    """
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        memo = [-1] * (n + 1)
        memo[1] = 1
        memo[2] = 2

        for num in range(3, n + 1):
            memo[num] = memo[num - 1] + memo[num - 2]

        return memo[n]
