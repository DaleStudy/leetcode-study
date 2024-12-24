class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for _ in range(31) :
            ret |= n & 1
            ret <<= 1
            n >>= 1
        ret += n & 1
        return ret
