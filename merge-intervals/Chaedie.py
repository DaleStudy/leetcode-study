"""
Time: O(n log(n))
Space: O(n)
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            prev = result[-1]

            if prev[0] <= start <= prev[1]:
                result[-1][1] = max(prev[1], end)
            else:
                result.append([start, end])
        return result
