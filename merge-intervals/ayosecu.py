from typing import List

class Solution:
    """
        - Time complexity: O(nlogn), n = len(intervals)
        - Space Complexity: O(1), If output variable excluded.
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result
    

tc = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]])
]

solution = Solution()
for i, (intervals, e) in enumerate(tc, 1):
    r = solution.merge(intervals)
    print(f"TC {i} is Passed!" if r == e else f"TC 1 is Failed! - Expected: {e}, Result: {r}")
