# time complexity O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:].zfill(32)
        reversed_binary = binary[::-1]
        return int(reversed_binary, 2)
