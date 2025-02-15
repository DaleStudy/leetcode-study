class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_string = bin(n).replace('0b', '');
        return binary_string.count('1');
