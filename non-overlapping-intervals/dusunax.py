'''
# 435. Non-overlapping Intervals

## understanding the problem
- 겹치지 않는 인터벌을 최대한 많이 남기기 위해, 지워야하는 인터벌의 최소값 반환
- not it: 그래프에 순환이 있는지 여부를 알아본다❌ overkill
- core approach: Greedy 

## Greedy
- Whenever you detect an overlap, you should remove one.
    - not physically. we'll going to return counts, so just keep counts is enough.
- Goal: keep many non-overlapping intervals as possible to minimize removal.

### how to detect overlap?
1. sort intervals by ends
2. iterate through intervals while tracking down the prev_end(last vaild end time)
  - if `current_start < prev_end`, it's overlap.
    - Example: 
      - [2, 4] is overlap with [1, 3]
      - start (2) is smaller than end (3)

### which one should removed?
- when overlap happens, remove the interval that ends later 
  - it will restrict more future intervals.
    - the longer an interval lasts, the more it blocks others(leaving less room for non-overlapping intervals)

## complexity

### TC is O(n log n)
- sorting: O(n log n)
- iterating: O(n)
- total: O(n log n)

### SC is O(1)
- no extra space is used
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        count = 0 # number of removals
        prev_end = intervals[0][1] # last valid end time
        
        for start, end in intervals[1:]: # 1 ~ n-1
            if start < prev_end: # overlap detected
                count += 1 
                # <do NOT move the prev_end pointer>
                # prev_end is still pointing at the previous interval 
                # so it's keeping the interval ends earlier. (removing the longer one)
            else: 
                prev_end = end
        
        return count
