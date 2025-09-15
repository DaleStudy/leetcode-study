# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# time complexity O(n), space complexity O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # 뒤집힌 리스트의 시작 노드
        curr = head # 현재 탐색 중인 노드

        while curr:
            temp = curr.next # 다음 노드 기억
            curr.next = prev
            # 다음 포인터로 이동하기 전 현재노드를 이전 노드로 변경
            prev = curr
            # 포인터 이동
            curr = temp

        return prev

# time complexity O(n), space complexity O(n)
# class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     stack = []
    #     while head:
    #         stack.append(head)
    #         head = head.next
    #
    #     dummy = ListNode()
    #     curr = dummy
    #     while stack:
    #         node = stack.pop()
    #         node.next = None
    #         curr.next = node
    #         curr = curr.next
    #
    #     return dummy.next
