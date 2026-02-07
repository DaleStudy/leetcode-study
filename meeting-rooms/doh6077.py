
# https://neetcode.io/problems/meeting-schedule/question
# Related Question 
# https://leetcode.com/problems/non-overlapping-intervals/description/
# 이전에 풀었던 문제와 상당히 비슷하다고 생각해서 해당 문제를 풀었던 풀이대로 풀었다. 
# 1. Sort the input by start time
# 2. Track the previous interval's end time
# 3. Check if the current interval's start overlaps with the previous end
# Time complexity: O(n log n)
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        if not intervals:
            return True
        
        intervals.sort(key=lambda x: x.start)
        
        prev = intervals[0].end
        
        for i in intervals[1:]:
            if i.start >= prev:
                prev = i.end
            else:
                return False
        return True
    # for i in range(1, len(intervals)):
    #     i1 = intervals[i-1]
    #     i2 = intervals[i]

    #     if i1.end > i2.start:
    #         return False 
