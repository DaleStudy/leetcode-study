# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            tmp = curr.next ## save next node
            curr.next = prev ## reverse next pointer to the prev
            prev = curr ## update prev pointer with curr, since it's reversed now
            curr = tmp ## move on to the next saved node

        return prev

        ## TC: O(n) SC: O(1)
