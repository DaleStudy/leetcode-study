class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for interval in sorted(intervals):
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
