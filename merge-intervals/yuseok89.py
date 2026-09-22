# TC: O(NlogN)
# SC: O(N)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        ans = list()

        intervals.sort(key=lambda x:x[0])

        ans.append([intervals[0][0]])

        end = intervals[0][1]

        for idx in range(1, len(intervals)):
            if intervals[idx][0] <= end:
                end = max(end, intervals[idx][1])
            else:
                ans[-1].append(end)
                ans.append([intervals[idx][0]])
                end = intervals[idx][1]

        ans[-1].append(end)

        return ans

