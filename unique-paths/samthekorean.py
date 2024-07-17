# TC : O(n)
# SC : O(1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, n - 1)
