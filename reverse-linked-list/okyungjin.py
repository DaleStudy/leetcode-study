# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Time: O(N)
Space O(N)
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        stack = []

        while head:
            stack.append(head)
            head = head.next

        dummy_head = ListNode()
        curr = dummy_head
        
        while stack:
            curr.next = stack.pop()
            curr = curr.next

        curr.next = None

        return dummy_head.next


"""
Time: O(N)
Space O(1)
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        return prev
