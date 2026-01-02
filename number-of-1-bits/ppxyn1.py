# idea: - 

from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = bin(n).split('0b')[-1]
        return Counter(bits)['1']



