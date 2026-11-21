# Time Complexity: O(n)
# Space Complexity: O(1)
# With 1 <= n <= 45, all counts fit within a 32-bit signed integer.
# Approach: Build each count by adding the previous two counts.
#
# Solution history
# 1. Counted arrangements using C(n - k, k) for each possible k.
# 2. Replaced combination calls with additions of the previous two counts.
#    Keeps only two values. Current solution.
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev, curr = 1, 2

        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr

        return curr


# Previous solution (Attempt 1: Combinations)
# Time Complexity: O(n)
# Space Complexity: O(1)
# These bounds assume 1 <= n <= 45, where CPython's math.comb
# uses fixed-size integer fast paths and all values remain small.
#
# from math import comb
#
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         step = 0
#         for k in range(n // 2 + 1):
#             step += comb(n - k, k)
#
#         return step

