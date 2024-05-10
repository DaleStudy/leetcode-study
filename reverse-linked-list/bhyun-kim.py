"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/description/

Solution
    Iteratively reverses a singly linked list.

    1. Initialize two pointers, prev and curr, to None and the head of the linked list, respectively.
    2. While curr is not None:
        a. Save the next node of curr.
        b. Set the next node of curr to prev.
        c. Move prev and curr to the next nodes.

Time complexity: O(n)
Space complexity: O(1)

"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        return prev
