from heapq import heappush, heappop
from typing import List, Optional
from unittest import TestCase, main


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        return self.solve(head)

    """
    Runtime: 15 ms (Beats 88.30%)
    Time Complexity: O(n)
        - 역방향 링크드 리스트인 backward를 생성하는데, 원본 링크드 리스트의 모든 노드를 조회하는데 O(n)
        - reorder하는데 원본 링크드 리스트의 모든 노드의 길이만큼 backward와 forward의 노드들을 조회하는데 O(n)
        > O(n) + O(n) = 2 * O(n) ~= O(n)

    Memory: 23.20 MB (Beats 88.27%)
    Space Complexity: O(n)
    > 역방향 링크드 리스트인 backward를 생성하는데, backward의 길이는 원본 링크드 리스트의 길이와 같으므로 O(n)
    """
    def solve(self, head: Optional[ListNode]) -> None:
        backward = ListNode(head.val)
        backward_node = head.next
        length = 1
        while backward_node:
            length += 1
            temp_node = ListNode(backward_node.val)
            temp_node.next = backward
            backward = temp_node
            backward_node = backward_node.next

        node = head
        forward = head.next
        for i in range(length):
            if i == length - 1:
                node.next = None
                return

            if i % 2 == 0:
                node.next = backward
                backward = backward.next
                node = node.next
            else:
                node.next = forward
                forward = forward.next
                node = node.next


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        node_1 = ListNode(1)
        node_2 = ListNode(2)
        node_3 = ListNode(3)
        node_4 = ListNode(4)
        node_5 = ListNode(5)
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5

        self.assertEqual(Solution().reorderList(node_1), True)


if __name__ == '__main__':
    main()
