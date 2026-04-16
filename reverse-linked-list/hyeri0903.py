# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None

        st = []
        cur = head

        while cur:
            st.append(cur.val)
            cur = cur.next
        
        dummy = ListNode(0)
        cur = dummy

        while st:
            cur_value = st.pop()
            cur.next = ListNode(cur_value)
            cur = cur.next

        return dummy.next



        