'''
# 1. Two Sum

use a hash map to store the numbers and their indices.
iterate through the list and check if the complement of the current number (target - nums[i]) is in the hash map.

(assume that each input would have exactly one solution)
- if it is a pairNum, return the indices of the two numbers.
- if it is not, add the current number and its index to the hash map.


## Time and Space Complexity

```
TC: O(n)
SC: O(n)
```

#### TC is O(n):
- iterating through the list just once to find the two numbers. = O(n)

#### SC is O(n):
- using a hash map to store the numbers and their indices. = O(n)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            pairNum = target - nums[i]
            if pairNum in map:
                return [map.get(pairNum), i]
            map[nums[i]] = i