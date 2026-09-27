"""
시간복잡도: O(n log n)
  - n: 입력된 배열 intervals의 길이
공간복잡도: O(n)
  - n: 진행 중인 회의의 종료 시각을 저장하는 최소 힙의 크기

intervals를 시작 시각 기준으로 정렬합니다.
최소 힙에는 아직 사용 중인 회의실의 종료 시각을 저장합니다.

각 회의의 시작 시각이 힙의 가장 이른 종료 시각 이후이면
그 회의실은 비었으므로 힙에서 제거하고,
현재 회의의 종료 시각을 힙에 넣습니다.
힙 크기의 최댓값이 필요한 최소 회의실 개수입니다.
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 1
        heap = []

        for start, end in intervals:
            while heap and heap[0] <= start:
                heappop(heap)
            heappush(heap, end)
            ans = max(ans, len(heap))

        return ans
