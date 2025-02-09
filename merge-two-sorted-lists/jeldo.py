class Solution:
    # O(n+m), n = len(list1), m = len(list2)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        if list1:
            node.next = list1
        if list2:
            node.next = list2
        return head.next
