# Goal: Given a positive int n, return the number of set bits in binary.
# Approach:
# Divide by 2 and check the remainder to determine the last bit.
# If the remainder is 1, update the variable 'count'.
# Repeat until n becomes 0.
# Time Complexity: O(logn)
# - We process each bit of n.
# Space Complexity: O(1)
# - We use only one variable 'count'.
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n != 0:
            if n % 2 == 1:
                count += 1
            n = n // 2
        
        return count
