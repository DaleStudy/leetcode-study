"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Solution
    Recursively merges two sorted linked lists.
    
    1. Check if either list is empty.
    2. Compare the values of the two lists.
    3. Return a new node with the smaller value and the merged list.

Time complexity: O(n)
Space complexity: O(n)
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        if list1.val < list2.val:
            val = list1.val
            list1 = list1.next
        else:
            val = list2.val
            list2 = list2.next

        return ListNode(val=val, next=self.mergeTwoLists(list1, list2))
