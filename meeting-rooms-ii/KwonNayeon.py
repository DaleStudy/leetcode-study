"""
Time Complexity: O(n log n)
- 정렬에 O(n log n)
- 각 미팅에 대한 힙 연산이 O(log n)

Space Complexity: O(n)
- 최악의 경우 모든 미팅이 동시에 진행되어 힙에 n개의 원소가 저장됨

풀이방법:
1. 미팅 시간(intervals)을 시작 시간을 기준으로 정렬함
2. 최소 힙을 이용해서 현재 진행 중인 미팅의 종료시간을 저장함
3. 각 미팅을 순회하면서:
  - 새 미팅의 시작시간이 힙의 최소 종료시간보다 크거나 같으면 -> 가장 일찍 끝나는 미팅을 힙에서 제거
  - 현재 미팅의 종료시간을 힙에 추가
4. 힙의 크기 = 필요한 최소 회의실의 수
"""
import heapq

def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    rooms = []

    heapq.heappush(rooms, intervals[0][1])

    for i in range(1, len(intervals)):
        if intervals[i][0] >= rooms[0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, intervals[i][1])
    return len(rooms)

