"""
https://leetcode.com/problems/merge-k-sorted-lists/description/

문제: k개의 링크드 리스트가 주어지고, 각 링크드 리스트가 오름차순으로 정렬이 되어있다.
     모든 링크드 리스트를 병합하여 하나의 정렬된 링크드 리스트를 만들어라.

풀이:
    heapq를 쓰면 항상 가장 작은 값을 O(log k) 시간에 꺼낼 수 있음.
    heapq -> '최소 힙 구조' -> 내부적으로 항상 가장 작은 값이 루트에 오도록 정렬됨.

    1. 각 리스트의 첫 노드를 heap에 넣음 (val, 고유번호, 노드)
    2. heap에서 가장 작은 값 꺼내면서 결과 리스트 구성
    3. 다음 노드를 힙에 추가

n = 모든 노드의 총 개수
k = 연결 리스트의 개수

TC: O(n log k)
- n개의 노드를 각각 힙에 1번씩 push, 1번씩 pop함 → 총 2n번 힙 연산
- 각 힙 연산은 log k 시간 (힙 크기 최대 k)

SC: O(k)
- 힙에 최대 k개의 노드가 동시에 들어감
"""

from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # 1. 각 리스트의 첫 노드를 heap에 넣음 (val, 고유번호, 노드)
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))

        dummy = curr = ListNode(-1)

        # 2. heap에서 가장 작은 값 꺼내면서 결과 리스트 구성
        while heap:
            val, idx, node = heapq.heappop(heap)  # 가장 작은 노드 꺼내기
            curr.next = node                      # 결과 리스트에 붙이기
            curr = curr.next                      # 다음 노드로 이동

            if node.next:
                # 다음 노드를 힙에 추가
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return dummy.next
