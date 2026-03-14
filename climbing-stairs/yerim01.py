# Goal: Given n steps, return the number of distinct ways you can climb to the top.
# Constraints:
# - You can climb either 1 or 2 steps at each time.
# - 1 <= n <= 45
# Approach:
# f(n) = number of ways to reach step n.
# The last move must be from step n-1 or step n-2.
# Therefore, f(n) = f(n-1) + f(n-2).
# Base case - f(1) = 1, f(2) = 2.
# Use two variables prev1&prev2 to track the number of of f(n-1)&f(n-2).
# Iterate a loop, staring from 3.
# Store prev1 into temp.
# Update prev1&prev2.
# Return prev1.

# Time complexity: O(n)
# - We iterate once
# Space complexity: O(1)
# - Only using variables

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev1 = 2
        prev2 = 1

        for i in range(3, n+1):
            temp = prev1
            prev1 = prev2 + prev1
            prev2 = temp
        
        return prev1
