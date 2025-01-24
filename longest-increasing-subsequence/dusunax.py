'''
# 300. Longest Increasing Subsequence

use the sub list to store current LIS.
iterate nums's elements and find the position of the current number in the subsequence. (using a binary search helper function)
after the iteration finishes, return the length of the subsequence.

> **helper function explanation:**
> ```py
> position = bisectLeft(sub, num)
> ```
> bisectLeft is doing binary search that finds the leftmost position in a sorted list.
>if the position is the end of the subsequence, append the current number to the subsequence.
>if the position is not the end of the subsequence, replace the number at the position with the current number.

> **python's bisect module:**
> https://docs.python.org/3.10/library/bisect.html

## Time and Space Complexity

```
TC: O(n log n)
SC: O(n)
```

#### TC is O(n log n):
- iterating through the nums list to find the position of the current number. = O(n)
- using a binary search helper function to find the position of the current number. = O(log n)

#### SC is O(n):
- using a list to store the subsequence. = O(n) in the worst case
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [] # SC: O(n)
        
        for num in nums: # TC: O(n)
            pos = self.bisectLeft(sub, num) # bisect.bisect_left(sub, num) = TC: O(log n)
            if pos == len(sub):
                sub.append(num)
            else:
                sub[pos] = num
        
        return len(sub)
    
    def bisectLeft(self, list, target) -> int:
        low = 0
        high = len(list) - 1

        while low <= high :
            mid = int(low + (high - low) / 2) 

            if list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low
