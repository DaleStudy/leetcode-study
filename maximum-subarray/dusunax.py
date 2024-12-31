'''
# 53. Maximum Subarray

- use Kadane's Algorithm for efficiently finding the maximum subarray sum.

## Time and Space Complexity

```
TC: O(n)
SC: O(1)
```

#### TC is O(n):
- iterating through the list just once to find the maximum subarray sum. = O(n)

#### SC is O(1):
- using a constant amount of extra space to store the current sum and the maximum sum. = O(1)
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        currentSum = 0 # SC: O(1)
        maxSum = nums[0] # SC: O(1)

        for i in range(len(nums)): # TC: O(n)
            currentSum = max(currentSum + nums[i], nums[i]) # TC: O(1)
            
            if currentSum > maxSum: # TC: O(1)
                maxSum = currentSum

        return maxSum
