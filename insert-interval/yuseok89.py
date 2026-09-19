#TC: O(N)
#SC: O(N)
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        ans = []
        is_processed = False

        for interval in intervals:
            if is_processed or interval[1] < newInterval[0]:
                ans.append(interval)
            elif newInterval[1] < interval[0]:
                ans.append(newInterval)
                ans.append(interval)
                is_processed = True
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        if not ans or ans[-1][1] < newInterval[0]:
            ans.append(newInterval)

        return ans

