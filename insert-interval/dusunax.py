'''
# 57. Insert Interval

use binary search to find the index of the new interval.(bisect_left)
insert the new interval into the list.
iterate through the list and merge the intervals.

=> insert first, merge later

## Time and Space Complexity

```
TC: O(n)
SC: O(n)
```

#### TC is O(n):
- do binary search to find correct index of the new interval. = O(log n)
- inserting the new interval into the list. = O(n)
- iterating through the list to merge the intervals. = O(n)

#### SC is O(n):
- using a list to store the intervals. = O(n)
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start_idx = bisect_left([interval[0] for interval in intervals], newInterval[0]) # TC: O(log n)
        
        intervals.insert(start_idx, newInterval) # TC: O(n)

        result = []  # SC: O(n)
        for interval in intervals: # TC: O(n)
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
            
        return result
