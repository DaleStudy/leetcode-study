class Solution:
    def hammingWeight(self, n: int) -> int:
        binaryString = bin(n)[2:]
        return list(binaryString).count("1")
