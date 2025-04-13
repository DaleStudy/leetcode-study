class Solution:
    def hammingWeight(self, n):
        return bin(n).count('1')
