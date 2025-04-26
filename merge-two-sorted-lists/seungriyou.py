# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            이미 list1, list2가 non-decreasing order로 정렬되어 있으므로, 각 linked list를 하나씩 비교하며 더 작은 값을 가진 노드부터 모으면 된다.
            그리고 list1, list2 중에 하나라도 다 본 경우, 남은 linked list를 끝에 붙이면 된다.
        """
        res = curr = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return res.next
