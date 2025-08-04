"""
시간 복잡도: O(1)
공간 복잡도: O(1)
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result
