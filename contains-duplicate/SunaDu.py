'''
# Leetcode 217. Contains Duplicate

use set to store distinct elements 🗂️

## Time and Space Complexity

```
TC: O(n)
SC: O(n)
```

### TC is O(n):
- iterating through the list just once to convert it to a set.

### SC is O(n):
- creating a set to store the distinct elements of the list.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

