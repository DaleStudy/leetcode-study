class Solution:
    def reverseBits(self, n: int) -> int:
        m = 0
        for i in range(32):
            remainder = n % 2
            n = n // 2
            m += pow(2, 31 - i) * remainder

        return m
