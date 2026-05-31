# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while head:
            temp.append(int(head.val))            
            head = head.next
        temp = list(reversed(temp))
        print(temp)
        
        dummy = ListNode(0)
        tail = dummy
        for i in temp:
            # print(i, tail)
            tail.next = ListNode(i)
            tail = tail.next
        # print(dummy)
        return dummy.next
