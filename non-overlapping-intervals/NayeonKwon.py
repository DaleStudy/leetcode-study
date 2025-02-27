"""
Constraints:
- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= starti < endi <= 5 * 10^4

Time Complexity: O(n * log n)
- 구간 정렬 시 O(n * log n) 사용, 정렬된 구간을 순회할 때 O(n)

Space Complexity: O(1)
- 정해진 변수 외에는 공간 사용하지 않음

풀이방법:
1. 끝점을 기준으로 오름차순 정렬 <- 제거할 구간의 수를 최소화하기 위해
2. 첫 번째 구간을 선택하고 그 구간의 끝점을 기록함
3. 두 번째 구간부터 end보다 시작점이 크거나 같은(겹치지 않는) 구간을 찾아서 카운트
4. 전체 구간의 수에서 count를 빼서 제거해야 할 구간의 수를 반환
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        count = 1
        end = intervals[0][1]

        for interval in intervals[1:]:

            if interval[0] >= end:
                count += 1
                end = interval[1]
                
        return len(intervals) - count

