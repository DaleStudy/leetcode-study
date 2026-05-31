# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = list1
        cur2 = list2

        answer = ListNode()
        head = answer


        while cur1 != None:
            if cur2 != None:
                if cur1.val >= cur2.val:
                    answer.next = ListNode(cur2.val)
                    cur2 = cur2.next
                    answer = answer.next
                else:
                    answer.next = ListNode(cur1.val)
                    cur1 = cur1.next
                    answer = answer.next
            else:
                answer.next = ListNode(cur1.val)
                cur1 = cur1.next
                answer = answer.next
        
        while cur2 != None:
            answer.next = ListNode(cur2.val)
            cur2 = cur2.next
            answer = answer.next
        return head.next
