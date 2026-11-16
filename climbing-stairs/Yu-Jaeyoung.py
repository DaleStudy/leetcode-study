from math import comb

# Time Complexity: O(n)
# Space Complexity: O(1)
# These bounds assume 1 <= n <= 45, where CPython's math.comb
# uses fixed-size integer fast paths and all values remain small.
# Approach: Sum C(n - k, k) for each possible number k of two-step moves.
#
# Solution history
# 1. Used combinations to choose the positions of k two-step moves
#    among n - k total moves. Current solution.
class Solution:
    def climbStairs(self, n: int) -> int:
        step = 0
        for k in range(n // 2 + 1):
            step += comb(n - k, k)

        return step

