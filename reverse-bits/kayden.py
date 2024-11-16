class Solution:
    # 시간복잡도: O(1)
    # 공간복잡도: O(1)
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = n & 1
            n = n >> 1
            res = res << 1
            res = res | bit

        return res
