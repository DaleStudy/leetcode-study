# Time Complexity: O(1) - fixed 32-bit operations, at most 32 iterations
# Space Complexity: O(1) - only uses a few integer variables

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask to keep numbers within range
        mask = 0xFFFFFFFF
        # max value for a signed 32-bit integer (2^31 - 1)
        MAX = 0x7FFFFFFF   

        # keep going until there's no carry left
        while b != 0:  
            # carry is AND operation, then shift left
            carry = (a & b) << 1 
            # XOR does the addition, keep it within 32 bits
            a = (a ^ b) & mask    
            # carry becomes the new b (loop continues if carry exists)
            b = carry & mask      

        # if a is greater than MAX, it's actually a negative number in 32-bit terms
        # convert it to proper negative representation
        return a if a <= MAX else ~(a ^ mask)  
