"""
143. Reorder List
https://leetcode.com/problems/reorder-list/
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Solution:
    To reorder the linked list, we can follow these steps:
    First, find the middle of the linked list using the slow and fast pointers.
    Reverse the second half of the linked list.
    Merge the first half and the reversed second half.

    1. Find the middle of the linked list using the slow and fast pointers
        - Initialize the slow and fast pointers to the head of the linked list
        - Move the slow pointer by one step and the fast pointer by two steps 
          until the fast pointer reaches the end of the linked list.
    2. Reverse the second half of the linked list
        - Initialize the prev and curr pointers to None and the middle node, respectively
        - Iterate through the second half of the linked list
            - Store the next node of the current node
            - Reverse the current node
            - Move the prev and curr pointers to the next nodes
    3. Merge the first half and the reversed second half
        - Initialize the first and second pointers to the head and the reversed second half, respectively
        - Iterate through the linked list
            - Store the next nodes of the first and second pointers
            - Update the next pointers of the first and second pointers
            - Move the first and second pointers to the next nodes

Time complexity: O(N)
    - We iterate through the linked list to find the middle node and reverse the second half
    - The time complexity is O(N)

Space complexity: O(1)
    - We only use constant extra space for the pointers
    - The space complexity is O(1)

"""


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        first, second = head, prev
        while second.next:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2