class Solution:
    def hammingWeight_v1(self, n: int) -> int:
        # Recursive solution 
        # Time complexity: O(log n)
        # Space complexity: O(log n) 
        if n == 0: return 0 
        elif n % 2 == 0: return self.hammingWeight(n // 2)
        else: return self.hammingWeight(n // 2) + 1 

    def hammingWeight(self, n: int) -> int:
        # Iterative solution
        # Time complexity: O(log n)
        # Space complexity: O(1)
        set_bit_cnt = 0 
        while n > 0: 
            set_bit_cnt += n & 1
            n >>= 1
        return set_bit_cnt
