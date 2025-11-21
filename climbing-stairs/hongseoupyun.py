
# This problem is a getting the number of cases to climb stairs just taking 1 or 2 steps at a time.
# The pattern is similar to Fibonacci sequence.
# As n increases by 1, the number of ways to climb will be 1, 2, 3, 5, 8, 13, 21
# The Formula is to get number of ways to climb to the nth step is:
# ways(n) = ways(n-1) + ways(n-2) with base of ways(1) = 1 and ways(2) = 2
# which means the number of ways to climb is the sum of last two previous ways



# Time complexity is O(n) - loops n times
# Space complexity is  O(1) — memorizes only prev1 & prev2
class Solution:
    def climbStairs(self, n: int) -> int:
        # Handling base case
        if n <= 1:
            return 1
        if n == 2:
            return 2
        
        prev1 = 1
        prev2 = 2
        for i in range(n,n+1):
            current = prev2 + prev1
            prev1 = prev2
            prev2 = current

        return prev2


            
        
        




        