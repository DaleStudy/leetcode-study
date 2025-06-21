# https://leetcode.com/problems/reorder-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            1. linked-list의 중간 지점을 찾은 후, left / right list를 나눈다.
            2. right list를 reverse 한다.
            3. left와 right에서 노드를 하나씩 가져와 연결한다.
        """

        # linked-list의 중간 지점을 찾은 후, left / right list 나누기
        slow = fast = head
        while fast and fast.next:
            slow = slow.next  # -> fast가 linked-list의 끝에 도달하면, slow는 중앙에 위치
            fast = fast.next.next

        # (slow부터 시작하는) right list를 reverse (w. 다중 할당)
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # left와 right list에서 노드를 각각 하나씩 가져와 연결 (w. 다중 할당)
        left, right = head, prev
        while right.next:
            left.next, left = right, left.next
            right.next, right = left, right.next
