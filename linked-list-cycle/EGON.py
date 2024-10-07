from typing import Optional
from unittest import TestCase, main


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.solve(head)

    """
    Runtime: 37 ms (Beats 93.02%)
    Time Complexity: O(n)
        > head부터 next가 있는 동안 선형적으로 조회하므로 O(n)

    Memory: 18.62 (Beats 98.22%)
    Space Complexity: O(1)
        > head를 제외하고 아무 변수도 사용하지 않았으므로 O(1)
    """
    def solve(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        while head.next:
            if head.next and head.next.val is None:
                return True

            head.val = None
            head = head.next

        return False


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        head = None
        output = False
        self.assertEqual(Solution().hasCycle(head), output)


if __name__ == '__main__':
    main()
