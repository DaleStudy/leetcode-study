from typing import Optional
from unittest import TestCase, main


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.solve(list1, list2)

    """
    Runtime: 36 ms (Beats 71.91%)
    Time Complexity: O(m + n)
        > list1의 길이를 m, list2의 길이를 n이라 할 때, list1과 list2 모두 끝까지 조회하므로 O(n + m)

    Memory: 16.62 (Beats 37.59%)
    Space Complexity: O(m + n)
        > result의 길이는 list1의 길이와 list2의 길이의 합과 같으므로 O(m + n) 
    """
    def solve(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        node = result
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    node = node.next
                    list1 = list1.next
                else:
                    node.next = list2
                    node = node.next
                    list2 = list2.next

            elif list1 and not list2:
                node.next = list1
                node = node.next
                list1 = list1.next

            elif not list1 and list2:
                node.next = list2
                node = node.next
                list2 = list2.next

            else:
                break

        return result.next


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        list1 = ListNode(
            val=1,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=4
                )
            )
        )
        list2 = ListNode(
            val=1,
            next=ListNode(
                val=3,
                next=ListNode(
                    val=4
                )
            )
        )
        output = [1,1,2,3,4,4]
        self.assertEqual(Solution.mergeTwoLists(Solution(), list1, list2), output)


if __name__ == '__main__':
    main()
