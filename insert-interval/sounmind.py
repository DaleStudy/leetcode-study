from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        new_start, new_end = newInterval

        for interval in intervals:
            current_start, current_end = interval

            if current_end < new_start:
                result.append(interval)

            else:
                if current_start > new_end:
                    result.append([new_start, new_end])
                    new_start, new_end = interval

                else:
                    new_start = min(new_start, current_start)
                    new_end = max(new_end, current_end)

        result.append([new_start, new_end])

        return result
