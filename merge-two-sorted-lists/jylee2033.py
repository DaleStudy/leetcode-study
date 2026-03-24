# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Use a while loop to compare values and build the merged list

        # Create a new list
        output = ListNode()
        cur = output

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next

        # Attach the remaining nodes
        cur.next = list1 or list2

        return output.next

# Time Complexity : O(n + m), n - lenght of list1, m - length of list2
# Space Complexity : O(1)
