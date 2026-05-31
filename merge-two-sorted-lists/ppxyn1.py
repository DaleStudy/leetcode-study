# idea : Two Pointer
# It was first time solving a two-pointer problem using nodes instead of arrays, and I realized I'm still not very familiar with nodes yet.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        node = dummy
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return dummy.next


# Another way to solve it
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not (list1 and list2):
#             return list1 or list2
#         if list1.val < list2.val:
#             list1.next = self.mergeTwoLists(list1.next, list2)
#             return list1
#         else:
#             list2.next = self.mergeTwoLists(list1, list2.next)
#             return list2


