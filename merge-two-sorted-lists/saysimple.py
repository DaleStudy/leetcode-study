# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# TC, SC: O(n), O(n)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 and list2):
            return list1 if list1 else list2

        ret = ListNode(0, None)
        head = ret

        while list1 and list2:
            a, b = list1.val, list2.val
            print(a, b)

            if a < b:
                print(1)
                next = ListNode(a, None)
                ret.next = next
                ret = next
                list1 = list1.next
            elif a > b:
                print(2)
                next = ListNode(b, None)
                ret.next = next
                ret = next
                list2 = list2.next
            else:
                for i in range(2):
                    next = ListNode(a, None)
                    ret.next = next
                    ret = next
                list1, list2 = list1.next, list2.next
            print(head)

        if list1:
            while list1:
                next = ListNode(list1.val, None)
                ret.next = next
                ret = next
                list1 = list1.next

        if list2:
            while list2:
                next = ListNode(list2.val, None)
                ret.next = next
                ret = next
                list2 = list2.next

        head = head.next

        return head
