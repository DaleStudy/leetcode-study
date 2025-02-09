'''
# 11. Container With Most Water

use two pointers to find the maximum area.

> **move the shorter line inward:**
> - area is determined by the shorter line.
> - move the shorter line inward => may find a taller line that can increase the area.

## Time and Space Complexity

```
TC: O(n)
SC: O(1)
```

### TC is O(n):
- while loop iterates through the height array once. = O(n)

### SC is O(1):
- using two pointers and max_area variable. = O(1)
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right: # TC: O(n)
            distance = right - left
            current_area = min(height[left], height[right]) * distance
            max_area = max(current_area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
