class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n, "032b")[::-1], 2)
    
