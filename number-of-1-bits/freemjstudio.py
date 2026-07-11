class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        return binary.count("1")
