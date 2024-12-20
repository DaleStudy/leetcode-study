'''
# Leetcode 15. 3Sum

use **two pointers** to solve this problem.

## Time and Space Complexity

```
TC: O(n^2)
SC: O(1)
```

### TC is O(n^2):
- sorting the list = O(n log n)
- iterating through the list and using two pointers to find the sum of three numbers. = O(n^2)

### SC is O(1):
- sorting in place = O(1)
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # TC: O(n log n), SC: O(1)
        result = [] # result are part of the output => do not count toward auxiliary (extra) space.
        
        for i in range(len(nums)): # TC: O(n^2)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            j = i + 1
            k = len(nums) - 1
            while j < k:
                currSum = nums[i] + nums[j] + nums[k]

                if currSum < 0:
                    j += 1
                elif currSum > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]]) 

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]: 
                        k -= 1

                    j += 1
                    k -= 1
        
        return result
