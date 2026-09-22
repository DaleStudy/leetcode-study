# 1) Iterate 32 times, getting the last bit of n and putting it to res using bitwise operators.
# TC: O(1)
# SC: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            bit = n & 1
            res = (res << 1) | bit
            n >>= 1
        return res
