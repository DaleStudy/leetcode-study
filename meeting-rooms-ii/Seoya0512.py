'''
Time Complexity: O(N log N)
- intervals.sort() 는 O(N log N) 소요
- 힙 자료구조 삽입과 pop에 O(log N) 소요

Space Complexity: O(N)
- ends 배열에 최악의 경우 N개의 원소가 들어갈 수 있음
'''
from typing import (
    List,
)
import heapq

def min_meeting_rooms(intervals: List) -> int:
  intervals.sort()
  ends = []

  for start,end in intervals:
    if ends and ends[0] <= start:
      heapq.heappop(ends)
    heapq.heappush(ends,end)
    
  return len(ends)
