"""
https://leetcode.com/problems/reverse-linked-list/

1. Stack 활용 (LIFO)
- LinkedList의 모든 원소를 Stack에 넣고 꺼냄
TC: O(n) time
SC: O(n) space

2. 최적화 풀이
- 현재 LinkedList를 거꾸로 뒤짚기
TC: O(n) -> LinkedList를 딱 한 번 순회
SC: O(1) -> 변수를 포인터 2개만 사용
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


"""
25/9/5 복습

링크드 리스트 뒤집기
=> 노드를 옮기는 것이 아니라, next 포인터의 방향을 바꾸면 된다!

TC: O(n)
SC: O(1)
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # 이전 노드
        curr = head  # 현재 노드

        while curr:
            next_node = curr.next  # 다음 노드 기억
            curr.next = prev       # 현재 노드의 방향을 반대로
            prev = curr            # 이전 노드를 한 칸 앞으로
            curr = next_node       # 현재 노드를 다음으로 이동

        # prev가 마지막 노드이자 새 head
        return prev
