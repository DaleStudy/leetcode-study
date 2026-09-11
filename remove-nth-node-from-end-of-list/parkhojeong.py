# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next

        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head
        i = 0
        while cur:
            if cnt - n == i:
                prev.next = cur.next
                break

            prev = cur
            cur = cur.next
            i += 1

        return dummy.next
