# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2: 
            return list1

        cursor = ListNode()
        result = cursor
        cursor.next = list1

        while cursor.next:
            while list2 and list2.val <= cursor.next.val:
                temp_1 = cursor.next
                temp_2 = list2.next

                cursor.next = list2
                list2.next = temp_1
                list2 = temp_2

            cursor = cursor.next
        
        if list2:
            cursor.next = list2

        return result.next
      
