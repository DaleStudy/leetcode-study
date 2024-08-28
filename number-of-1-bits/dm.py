class Solution:    
    def hammingWeight(self, n: int, acc: int = 0) -> int:
        if n == 0:
            return acc
        
        return self.hammingWeight(n // 2, acc + n % 2)
