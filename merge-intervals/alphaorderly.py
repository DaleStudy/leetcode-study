"""
시간복잡도: O(n log n)
공간복잡도: O(n)

1. 인터벌을 시작시간이 이른 순서대로 정렬한다.
2. 첫 번째 인터벌을 시작시간과 종료시간으로 설정한다.
3. 두 번째 인터벌부터 시작시간이 이전 인터벌의 종료시간보다 작거나 같은 경우 종료시간을 최대값으로 업데이트한다.
4. 그렇지 않은 경우 이전 인터벌을 결과에 추가하고 현재 인터벌을 시작시간과 종료시간으로 설정한다.
5. 마지막 인터벌을 결과에 추가한다.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        N = len(intervals)
        schedule = []

        start, end = intervals[0]

        for i in range(1, N):
            event_start, event_end = intervals[i]

            if event_start <= end:
                end = max(end, event_end)
            else:
                schedule.append([start, end])
                start = event_start
                end = event_end

        schedule.append([start, end])

        return schedule
