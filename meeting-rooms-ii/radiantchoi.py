import heapq

from typing import (
    List,
)

# Definition of Interval
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # 이 문제에서는 회의 시작과 끝 시간이 interval이라는 별개의 객체로 정의되어 있음
        # Meeting Rooms 문제처럼, 시작 시간을 기준으로 미리 정렬
        intervals.sort(key=lambda x: x.start)
        
        # 현재 회의가 진행중인 방 갯수
        rooms = []

        for current in intervals:
            # 초기 설정 - 사용중인 방이 없다면, 그냥 추가
            # 빈 배열이므로 heappush를 사용할 필요는 없다
            if not rooms:
                rooms.append(current.end)
            else:
                # 현재 진행 중인 회의 중 가장 빨리 끝나는 시간을 추출
                ending = heapq.heappop(rooms)

                # 현재 회의의 시작 시간이 가장 빨리 끝나는 회의보다 빠르다면, 해당 자리를 비울 수 없으므로 다시 힙에 삽입
                if current.start < ending:
                    heapq.heappush(rooms, ending)
                
                # 현재 회의가 끝나는 시간 삽입
                heapq.heappush(rooms, current.end)

        # 자연스럽게, 끝나는 시간들이 담긴 배열의 길이가 최소 회의실 갯수
        return len(rooms)
