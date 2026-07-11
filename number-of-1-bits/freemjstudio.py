class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        return binary.count("1")

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 

        while n > 0:
            count += n % 2
            n //=2
        
        return count