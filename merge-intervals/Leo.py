class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def sort_key(interval):
            return interval[0]

        intervals.sort(key=sort_key)

        result = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = result[-1][1]

            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end)
            else:
                result.append([start, end])

        return result

        ## TC: O(nlogn), SC: O(n)
