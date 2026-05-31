# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        if list1:
            head.next = list1
        elif list2:
            head.next = list2

        return dummy.next

"""
================================================================================
풀이 과정
================================================================================

[1차 시도] Dummy Node 활용
────────────────────────────────────────────────────────────────────────────────
1. 작은 값을 가진 노드를 골라서 head에 연결하는 방식으로 문제를 풀어보자.
2. 한 쪽 리스트가 비게 되면 남은 노드를 그냥 연결해주면 될 것 같음.

        dummy = ListNode()
        head = dummy

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        if list1:
            head.next = list1
        elif list2:
            head.next = list2

        return dummy.next
"""
