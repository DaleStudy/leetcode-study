"""
https://leetcode.com/problems/non-overlapping-intervals/

Time: O(N log N), intervals 정렬
Space: O(1)
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # end 오름차순 intervals 정렬
        intervals.sort(key=lambda x: x[1])

        # remove count
        count = 0        
        last_end = float('-inf')

        for start, end in intervals:
            if start >= last_end: # 구간 안 겹침
                last_end = end
            else: # 구간 겹침
                count += 1
            
        return count
