"""
Blind 75 - Merge Two Sorted Lists
LeetCode Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/
시간복잡도 : O(n+m)
공간복잡도 : O(1)
풀이 : (알고달레 답안)
각 링크드 리스트에 포인터를 두고, 더 작은 값을 가진 노드를 결과 리스트에 추가하다가 한 쪽 리스트가 끝나면 나머지 리스트를 결과 리스트에 추가한다.
마지막에 첫번째 노드를 반환한다.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
            
        tail.next = list1 or list2
        return dummy.next
    
