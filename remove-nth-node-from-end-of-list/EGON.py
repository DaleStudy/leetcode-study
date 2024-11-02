from typing import Optional
from unittest import TestCase, main


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def values(self) -> [int]:
        result = []
        node = self
        while node:
            result.append(node.val)
            node = node.next

        return result


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return self.solve_two_pointer(head, n)
    """
    Runtime: 0 ms (Beats 100.00%)
    Time Complexity: O(n)
    > list의 모든 node + dummy node를 탐색하므로 O(n + 1) ~= O(n)

    Memory: 16.62 MB (Beats 15.78%)
    Space Complexity: O(1)
    > 포인터만 사용하므로 O(1)
    """
    def solve_two_pointer(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        dummy = ListNode(-1)
        dummy.next = head
        head = dummy

        slow = fast = head
        while n:
            if fast.next:
                fast = fast.next
            n -= 1

        while fast is not None:
            if fast.next is None:
                slow.next = slow.next.next
                break
            else:
                slow = slow.next
                fast = fast.next

        return head.next


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

        n = 2
        output = [1, 2, 3, 5]
        self.assertEqual(Solution().removeNthFromEnd(node_1, n).values(), output)

    def test_2(self):
        node_1 = ListNode(1)
        n = 1
        output = []
        self.assertEqual(Solution().removeNthFromEnd(node_1, n).values(), output)

    def test_3(self):
        node_1 = ListNode(1)
        node_2 = ListNode(2)
        node_1.next = node_2
        n = 2
        output = [2]
        self.assertEqual(Solution().removeNthFromEnd(node_1, n).values(), output)


if __name__ == '__main__':
    main()
