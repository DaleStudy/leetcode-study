from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """링크드 리스트를 뒤집어서 역순의 링크드 리스트를 만드는 함수

        Args:
            head (Optional[ListNode]): 주어진 링크드 리스트

        Returns:
            Optional[ListNode]: 뒤집어진 링크드 리스트
        """
        if head is None or head.next is None:
            return head
        curr = head.next
        new_head = self.reverseList(head.next)
        curr.next = head
        head.next = None
        return new_head
