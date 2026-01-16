class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        res = 0
        for i in range(32):
            bit = n & 1
            res = res + bit
            res = res << 1
            n = n >> 1
        res = res >> 1
            
        return res
    
# Complexity O(1) - Time: 32 iterations, Space: O(1) no extra space used

