from heapq import heappush, heappop
from typing import List, Optional
from unittest import TestCase, main


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.solve_priority_queue(lists)

    """
    Runtime: 7 ms (Beats 100.00%)
    Time Complexity: O(n * m)
        - lists의 길이 k만큼 조회에 O(k)
            - 힙의 크기가 최대 k이므로, heappush에 * O(log k)
        - heap의 크기는 최대 k이므로, 
            - heappop하는데 O(k * log k)
            - heappush하는데 lists를 이루는 list를 이루는 모든 원소들의 총 갯수를 n이라 하면, O(n * log k)
        >  O(k * log k) + O(k * log k) + O(n * log k) ~= O(max(k, n) * log k) = O(n * log k)

    Memory: 19.44 MB (Beats 58.42%)
    Space Complexity: O(k)
        > heap의 크기는 lists의 길이 k에 비례하므로, O(k)
    """
    def solve_priority_queue(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heappop(heap)
            _, idx, result.next = node

            result = result.next
            if result.next:
                heappush(heap, (result.next.val, idx, result.next))

        return root.next


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    main()
