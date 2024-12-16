from typing import List, Optional
from unittest import TestCase, main


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def description(self) -> List[int]:
        desc = []
        node = self
        while node:
            desc.append(node.val)
            node = node.next

        return desc


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.solve_recursively(head)

    """
    Runtime: 41 ms (Beats 28.37%)
    Time Complexity: O(n)
        - Linked List의 모든 node를 순회하는데 O(n)
        - post 변수 할당, curr.next, prev와 curr의 참조 변경은 O(1)
        > O(n) * O(1) ~= O(n)

    Memory: 17.66 (Beats 85.13%)
    Space Complexity: O(1)
        - Linked List의 크기와 무관한 ListNode 타입의 prev, curr, post 변수를 할당하여 사용
        > O(1)
    """
    def solve_iteratively(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            post = curr.next
            curr.next = prev
            prev, curr = curr, post

        return prev

    """
    Runtime: 38 ms (Beats 50.06%)
    Time Complexity: O(n)
        - Linked List의 모든 node 만큼 재귀를 호출하므로 O(n)
        - post 변수 할당, curr.next의 참조 변경은 O(1)
        > O(n) * O(1) ~= O(n)

    Memory: 17.78 (Beats 27.88%)
    Space Complexity: O(n)
        > Linked List의 모든 node 만큼 reverse 함수가 스택에 쌓이므로 O(n)
    """
    def solve_recursively(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
            if not curr:
                return prev

            post = curr.next
            curr.next = prev
            return reverse(curr, post)

        return reverse(None, head)




class _LeetCodeTestCases(TestCase):
    def test_1(self):
        node1 = ListNode(val=1)
        node2 = ListNode(val=2)
        node3 = ListNode(val=3)
        node4 = ListNode(val=4)
        node5 = ListNode(val=5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        output = [5, 4, 3, 2, 1]
        self.assertEqual(Solution.reverseList(Solution(), node1).description(), output)


if __name__ == '__main__':
    main()
