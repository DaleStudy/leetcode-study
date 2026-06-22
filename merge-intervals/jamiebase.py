"""
# Approach
1. 현재 범위 & 비교 범위 변수
2. 비교 범위의 start가 현재 범위의 end보다 같거나 작으면 merge 가능
3. 최종 merge 범위를 현재 범위로 재갱신 & output 배열에 추가하는 방식

# Complexity
- Time complexity: intervals의 길이를 N, 정렬 때문에 O(N log N)
- Space complexity: output 배열이 최악의 경우 O(N)
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if (n := len(intervals)) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        output = []
        right = 1
        start, end = intervals[0]

        while right < n:
            comp_start, comp_end = intervals[right]
            if comp_start <= end:
                end = max(comp_end, end)
            else:
                output.append([start, end])
                start, end = comp_start, comp_end
            right += 1

        output.append([start, end])
        return output
