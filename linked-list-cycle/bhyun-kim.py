"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/description/

Solution
    Floyd's Tortoise and Hare algorithm:

    1. Initialize two pointers, slower and faster, to the head of the linked list.
        faster is one step ahead of slower.
    2. Move the slower pointer by one and the faster pointer by two.
    3. If the slower and faster pointers meet, return True.
    4. If the faster pointer reaches the end of the linked list, return False.

Time complexity: O(n)
Space complexity: O(1)
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not hasattr(head, "next"):
            return False

        slower = head
        faster = head.next

        while slower != faster:
            if not hasattr(faster, "next"):
                return False
            elif not hasattr(faster.next, "next"):
                return False
            slower = slower.next
            faster = faster.next.next

        return True
