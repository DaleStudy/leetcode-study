class Solution:
    # 시간복잡도: O(N+M) list1:N, list2: M
    # 공간복잡도: O(N+M)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        cur = merged

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            temp = temp.next

        if list1:
            cur.next = list1

        if list2:
            cur.next = list2

        return merged.next
