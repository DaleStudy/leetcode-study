# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Solution:
            1) 리스트1 리스트2가 null 이 아닌 동안 list1, list2를 차례대로 줄세운다.
            2) list1이 남으면 node.next = list1로 남은 리스트를 연결한다.
            3) list2가 남으면 list2 를 연결한다.

        Time: O(n)
        Space: O(1)
        """
        dummy = ListNode()
        node = dummy

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1
        elif list2:
            node.next = list2

        return dummy.next
