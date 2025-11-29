class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_num = format(n, 'b')
        return binary_num.count('1')
