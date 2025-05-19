# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
1. Stack 활용 (LIFO)
- LinkedList의 모든 원소를 Stack에 넣고 꺼냄
TC: O(n) time
SC: O(n) space

2. 최적화 풀이
- 현재 LinkedList를 거꾸로 뒤짚기
TC: O(n) -> LinkedList를 딱 한 번 순회
SC: O(1) -> 변수를 포인터 2개만 사용
"""

# Stack 풀이
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head
        while node:
            stack.append(node)
            node= node.next

        dummy = ListNode(-1)
        node = dummy
        while stack:
            node.next = stack.pop()
            node = node.next
        node.next = None
        return dummy.next
    
# 최적화
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev, curr = curr, temp_next
        return prev
