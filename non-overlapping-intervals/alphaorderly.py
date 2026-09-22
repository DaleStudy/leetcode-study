"""
# 시간 복잡도: O(n log n)
# 공간 복잡도: O(1)
#
# 1. 인터벌을 끝점을 기준으로 오름차순 정렬한다.
# 2. 첫 번째 인터벌의 끝점을 기준으로 순회하면서,
#    다음 인터벌의 시작점이 현재 끝점보다 작으면 겹치는 것으로 간주하여 카운트를 증가시킨다.
#    - 겹치면(count += 1) 끝점은 그대로 둔다.
#    - 겹치지 않으면 끝점을 현재 인터벌의 끝점으로 업데이트한다.
# 3. 마지막에 카운트를 반환한다.
#
# 왜 최선인가?
# - 끝점이 가장 작은 것부터 남겨두면 이후로 더 많은 인터벌을 남길 수 있다.
# - 이는 최대한 많은 인터벌을 남기기 위해 최소 개수의 인터벌만 제거하게 되는 그리디 전략이다.
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda k: k[1])
        N = len(intervals)

        count = 0
        end = intervals[0][1]

        for i in range(1, N):
            event_start, event_end = intervals[i]

            if event_start < end:
                count += 1
            else:
                end = event_end

        return count
