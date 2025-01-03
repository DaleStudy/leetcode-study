'''
# 238. Product of Array Except Self

use prefix and suffix to calculate the product of the array, except self.

## Time and Space Complexity

```
TC: O(n)
SC: O(n)
```

### TC is O(n):
- iterating through the list twice, to calculate both prefix and suffix products. = O(n)

### SC is O(n):
- storing the prefix and suffix in the answer list. = O(n)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # prefix
        for i in range(1, n):
            answer[i] *= nums[i - 1] * answer[i - 1]

        # suffix
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]

        return answer
