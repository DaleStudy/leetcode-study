class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 1
        while (n//2 != 0):
            remainder = n % 2
            if (remainder==1):
                result+=1
            n = n//2
        return result