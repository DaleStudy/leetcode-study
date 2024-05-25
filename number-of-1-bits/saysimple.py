# TC: O(1), SC: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
