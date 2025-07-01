"""
https://neetcode.io/problems/meeting-schedule-ii

주어지는 회의 시간 리스트 intervals = [[s₁, e₁], [s₂, e₂], ...] (각 si < ei)에 대해,
동시에 진행되는 회의의 최대 개수, 즉 필요한 최소 회의실 개수를 계산하는 문제

TC: O(N log N), 회의 시간 정렬 O(N log N)
SC: O(N), 배열 사용
"""

#Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # 회의 시작 시간과 종료 시간을 저장하는 배열
        start_times = [interval.start for interval in intervals]
        end_times = [interval.end for interval in intervals]

        # 시작 시간과 종료 시간을 정렬
        start_times.sort()  
        end_times.sort()

        # 회의실 개수 초기화
        rooms = 0
        end_index = 0

        # 각 회의 시작 시간을 순회하며 회의실 개수 계산
        for start in start_times:
            # 현재 회의 시작 시간이 이전 회의 종료 시간보다 크거나 같으면 회의실 개수 줄이기
            if start >= end_times[end_index]:
                rooms -= 1
                end_index += 1
            rooms += 1

        return rooms



"""
힙 풀이

TC: O(N log N), 회의 시간 정렬 O(N log N)
SC: O(N), 최악의 경우 모든 회의가 겹침
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x.start)

        heap = []

        for interval in intervals:
            start = interval.start
            end = interval.end

            # 현재 회의의 시작 시간 >= 가장 빨리 끝나는 회의의 종료 시간이라면
            # 그 회의실은 다시 사용할 수 있으므로 heap에서 제거 (pop)
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            
            # 새 회의의 종료 시간을 힙에 추가
            heapq.heappush(heap, end)

        # 힙에 남아 있는 종료 시간 수 = 동시에 진행 중인 회의 수 = 필요한 최소 회의실 수
        return len(heap)
