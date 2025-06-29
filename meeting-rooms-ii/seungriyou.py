# https://leetcode.com/problems/meeting-rooms-ii/

from typing import List

class Solution:
    def minMeetingRooms_heap(self, intervals: List[List[int]]) -> int:
        """
        [Complexity]
            - TC: O(nlogn) (sort & heappop/push)
            - SC: O(n) (min heap)

        [Approach]
            기본적으로 회의 시작 시각이 빠른 순서로 살펴보아야 한다.
            시작 시각 이전에 어떤 회의실이 빈다면 해당 회의실을 이어서 사용할 수 있고
            시작 시각 이후까지 기존 회의가 마치지 않는다면 해당 회의실을 사용할 수 없다.
            이를 매번 빠르게 판단하기 위해서는 그리디하게
                "이전까지 회의실을 사용하던 회의 중 가장 빨리 마치는 회의의 종료 시각"과 "현재 보고 있는 회의 시작 시각"
            을 비교하면 된다.
            항상 회의의 종료 시각 중 가장 작은 값을 고르면 되므로, min heap을 이용하여 최솟값을 O(1)에 조회할 수 있도록 할 수 있다.
        """
        import heapq

        # 회의 시작 시각 순으로 오름차순 정렬
        intervals.sort()

        # min heap
        rooms = []

        for s, e in intervals:
            # "이전까지 회의실을 사용하던 회의 중 가장 빨리 마치는 회의의 종료 시각"과 "현재 보고 있는 회의 시작 시각"이 겹치지 않는 경우,
            # rooms에 존재하는 회의실 중 e가 가장 이른 회의실 pop
            if rooms and rooms[0] <= s:
                heapq.heappop(rooms)

            # 현재 회의 push
            heapq.heappush(rooms, e)

        return len(rooms)

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        [Complexity]
            - TC: O(nlogn)
            - SC: O(n)

        [Approach]
            start와 end를 나누어 정렬한다면, 각각의 원소를 가리키는 two-pointer를 이용해
            회의실을 재사용할 수 있는 경우와 새로운 회의실이 필요한 경우를 판단할 수 있다.
            starts를 순회하면서 e라는 pointer로 ends의 첫번째 원소부터 비교하면 다음과 같이 케이스를 나눌 수 있다.
                - non-overlap(ends[e] <= s): 회의실 재사용 가능 (e++를 통해 다음 회의 살펴보기)
                - overlap(ends[e] > s): 새로운 회의실 필요
        """
        starts = sorted(s for s, _ in intervals)
        ends = sorted(e for _, e in intervals)

        res = e = 0

        for s in starts:
            # non overlap   -> 회의실 재사용 가능 (다음 회의 살펴보기)
            if ends[e] <= s:
                e += 1
            # overlap       -> 새로운 회의실 필요
            else:
                res += 1

        return res
