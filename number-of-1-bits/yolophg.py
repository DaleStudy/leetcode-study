# Time Complexity: O(k) - check each bit of n once. In the worst case, this is about 32 iterations.
# Space Complexity: O(1) - only use a constant amount of extra space.

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        # keep going till n becomes 0 (no more bits left to check)
        while n:
            # check if the last bit is 1 (n % 2 tells us this) and add it to the count
            count += (n % 2)
            # shift n to the right by 1 to move to the next bit
            n = n >> 1
        
        return count
