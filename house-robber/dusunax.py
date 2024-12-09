'''
# Leetcode 198. House Robber

use **dynamic programming** to solve this problem. (bottom-up approach) 🧩

choose bottom-up approach for less space complexity.

## DP relation

```
dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
```

- **dp[i - 1]:** skip and take the value from the previous house
- **dp[i - 2]:** rob the current house, add its value to the maximum money from two houses before

## Time and Space Complexity

```
TC: O(n)
SC: O(n)
```

### TC is O(n):
- iterating through the list just once to calculate the maximum money. = O(n)

### SC is O(n):
- using a list to store the maximum money at each house. = O(n)

'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            
        return dp[-1]
