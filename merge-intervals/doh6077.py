# 56. Merge Intervals

# First Try: 
# Time Complexity:O(N)
# Brute Force with Two Pointers
# 포인터를 사용해서 merge 해야하는 구간을 확인한다
# 효율적이지 않아서 더 나은 방법이 있을 거 같다. 해당 문제를 봤을때 일단 기본적으로 정렬을 하고 pointer를 사용하는 방법을 떠올렸다.
# merge 해야하는 구간은 2가지가 있다. 1. left의 end가 right의 start보다 크거나 같은 경우 2. left가 right의 구간을 전체를 다 포함하는경우 , 이경우 right를 지운다.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Use two pointers
        intervals = sorted(intervals)
        left, right = 0, 1 
        n = len(intervals)
        while left < right and right < n:
            if intervals[left][1] >= intervals[right][0] and intervals[left][1] >= intervals[right][1]:
                del intervals[right]
                n = len(intervals)
             # and intervals[left][1] < intervals[right][1]
            elif intervals[left][1] >= intervals[right][0]:
                intervals[left] = [intervals[left][0], intervals[right][1]]
                del intervals[right]
                n = len(intervals)
            # merge 할 경우가 아니면 다음 인덱스로 넘어가서 새로 비교한다 
            else:
                left += 1 
                right += 1
        return intervals 

        # Optimized Solution 
        intervals.sort(key=lambda interval: interval[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        
        return merged
