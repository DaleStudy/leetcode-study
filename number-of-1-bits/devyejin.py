class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += n % 2
            n //= 2
        return result
