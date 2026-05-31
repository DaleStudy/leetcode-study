# idea: - 
# Time Complexity: O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        # Ex,. newInterval = [2,5]
        for i in range(len(intervals)):
            start, end = intervals[i] 

            # [2,5] > [1,5] 

            # already passed
            if end < newInterval[0]: 
                res.append(intervals[i])

            # not started yet
            # (2)
            elif newInterval[1] < start: 
                res.append(newInterval) # [1,5]
                for j in range(i, len(intervals)):
                    res.append(intervals[j])
                return res
            else:
                # (1)
                # overlapping
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)

        res.append(newInterval)
        return res

