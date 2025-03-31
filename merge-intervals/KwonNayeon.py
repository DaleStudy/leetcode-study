"""
Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4

Time Complexity: O(nlogn)
- 정렬에 nlogn, 순회에 n이 필요하므로 전체는 O(nlogn)

Space Complexity: O(n)
- 최악의 경우 모든 구간이 겹치지 않아 n개의 구간을 저장해야 함

풀이방법:
0. intervals를 시작점 기준으로 정렬
1. merged 배열을 intervals의 첫 번째 구간으로 초기화
2. intervals의 두 번째 구간부터 순회하면서:
  - 현재 구간의 시작점이 merged 배열의 마지막 구간의 끝점보다 작거나 같으면 병합
  - 병합할 때는 끝점을 두 구간의 끝점 중 더 큰 값으로 설정
3. 현재 구간이 merged의 마지막 구간과 겹치지 않으면 그대로 merged에 추가
4. 2-3을 반복하여 모든 구간을 처리함
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])

            else:
                merged.append(interval)

        return merged

