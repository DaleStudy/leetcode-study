"""
스택에 모든 원소가 저장되어 있다면, 번갈아 가면서, 한 번은 링크드 리스트에서 노드를 얻고,
한 번은 스택에서 원소를 얻는다면, L[0] → L[n - 1] → L[1] → L[n - 2] → L[2] → L[n - 3] → … 순으로 노드에 접근할 수 있을 것

TC: O(n)
SC: O(n)
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        node = head
         # 연결 리스트의 모든 노드를 stack에 저장
        while node:
            stack.append(node)
            node = node.next
        
        node = dummy = ListNode(-1)
        for i in range(len(stack)):
            if i % 2:
                node.next = stack.pop()  # 홀수 인덱스: 뒤에서부터 꺼냄
            else:
                node.next = head         # 짝수 인덱스: 앞에서부터 가져옴
                head = head.next
            node = node.next
        node.next = None
        return dummy.next
