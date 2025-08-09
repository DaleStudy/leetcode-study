class Solution:
    @lru_cache
    def hammingWeight(self, n: int) -> int:
        return 1 + self.hammingWeight(n - (n & - n)) if n else 0
