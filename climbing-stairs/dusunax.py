'''
# Leetcode 70. Climbing Stairs

use `dynamic programming` to solve the problem.

1. Bottom-up approach
2. Top-down approach

## Time and Space Complexity

### 1. Bottom-up approach

```
TC: O(n)
SC: O(1)
```

#### TC is O(n):
- iterating with a for loop. O(n)

#### SC is O(1):
- using a constant space to store the previous two steps. O(1)

### 2. Top-down approach

```
TC: O(n)
SC: O(n)
```

#### TC is O(n):
- performing a recursive call for each step. O(n)

#### SC is O(n):
- using a memoization object to store the previous two steps. O(n)
'''

class Solution:
    '''
    1. Bottom-up approach
    '''
    def climbStairsLoop(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        # SC: O(1)
        prev2 = 1 # ways to step 0
        prev1 = 1 # ways to step 1 

        for i in range(3, n + 1): # TC: O(n)
            current = prev1 + prev2 # ways to (n-1) + (n-2)
            prev2 = prev1
            prev1 = current

        return prev1

    '''
    2. Top-down approach
    '''
    def climbStairsRecursive(self, n: int) -> int:
        memo = {} # SC: O(n)
        
        def dp(step: int, memo: int) -> int: # TC: O(n)
            if step == 1 or step == 2:
                memo[step] = step
            if step not in memo:
                memo[step] = dp(step - 1, memo) + dp(step - 2, memo) # ways to (n-1) + (n-2)
            return memo[step]

        return dp(n, memo)

