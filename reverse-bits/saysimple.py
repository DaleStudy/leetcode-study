class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f"{bin(n)[2:]:0>32}"[::-1], 2)
