'''
시간 복잡도: O(n)
- 중간 노드 찾기: O(n)
- 리스트 반전: O(n)
- 리스트 병합: O(n)

공간 복잡도: O(1)
- 포인터만 사용하여 링크를 조작하므로 O(1)
'''
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
        # find the middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse back half of the list
        prev, curr = None, slow.next
        slow.next = None # cut in the middle
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge front half with back half
        first, second = head, prev
        while second:
            first.next, second.next, first, second = second, first.next, first.next, second.next
