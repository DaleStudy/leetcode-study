# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy = head
        prev = None

        while dummy:
            nextNode = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = nextNode

        return prev

