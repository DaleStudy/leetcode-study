# 1) Recursion with memoization.
# TC: O(N) where N is the given natural number.
# SC: O(N) where N is the given natural number.
class Solution:
    def climb_rec(self, n: int, step: int, memo: Dict[int, int]):
        if step > n: return 0
        if step in memo: return memo[step]
        if step == n: return 1

        first_way = self.climb_rec(n, step + 1, memo)
        second_way = self.climb_rec(n, step + 2, memo)
        memo[step] = first_way + second_way
        return memo[step]
        

    def climbStairs(self, n: int) -> int:
        if n == 1: return 1

        memo = {}
        return self.climb_rec(n, 1, memo) + self.climb_rec(n, 2, memo)
