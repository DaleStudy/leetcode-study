class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0

        for i in range(32):
            if n & 1:
                res += 1 << (31 - i)
            n >>= 1

        return res

        # TC: O(1), SC: O(1) for both codes

        # n = bin(n)[2:].zfill(32)
        # return int(n[::-1], 2)
