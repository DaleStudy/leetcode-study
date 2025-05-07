from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merge two sorted linked lists and return the head of the merged list.

        Args:
            list1: Head of the first sorted linked list
            list2: Head of the second sorted linked list

        Returns:
            Head of the merged sorted linked list
        """
        # Handle edge cases
        if not list1:
            return list2
        if not list2:
            return list1

        # Create a dummy head to simplify the merging process
        dummy_head = ListNode()
        current = dummy_head

        # Merge nodes from both lists in sorted order
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach remaining nodes from either list
        current.next = list1 if list1 else list2

        return dummy_head.next
