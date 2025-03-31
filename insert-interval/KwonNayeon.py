"""
Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^5
- intervals is sorted by starti in ascending order.
- newInterval.length == 2
- 0 <= start <= end <= 10^5

Time Complexity: O(n)
- 모든 interval을 한 번씩만 처리함

Space Complexity: O(n)
- 최악의 경우 모든 interval을 결과 리스트에 저장

풀이방법:
1. 세 단계로 구분하여 처리:
  - Step 1: newInterval보다 앞에 있는 intervals → 결과에 바로 추가
  - Step 2: newInterval과 겹치는 intervals → 병합하여 하나의 interval로 만듦
  - Step 3: newInterval보다 뒤에 있는 intervals → 결과에 바로 추가
2. 병합 조건:
  - 두 interval이 겹치는 조건: intervals[i][0] <= mergedInterval[1]
  - 병합 시 시작점: min(mergedInterval[0], intervals[i][0])
  - 병합 시 끝점: max(mergedInterval[1], intervals[i][1])

노트: 
- 세 단계로 구분하여 처리하는 게 쉽지 않았다. 다음에 풀 땐 스스로 해결해볼 것
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        merged_interval = newInterval
        while i < n and intervals[i][0] <= merged_interval[1]:
            merged_interval[0] = min(merged_interval[0], intervals[i][0])
            merged_interval[1] = max(merged_interval[1], intervals[i][1])
            i += 1
        result.append(merged_interval)

        while i < n:
            result.append(intervals[i])
            i += 1

        return result
