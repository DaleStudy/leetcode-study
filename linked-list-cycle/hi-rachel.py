# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
TC: O(n)
SC: O(n)
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            # 해당 노드 이미 방문한 적 있으면
            if head in visited:
                return True
            # 방문한 적 없으면 set에 넣기
            visited.add(head)
            # 다음 노드로 이동
            head = head.next

        # cycle이 없음
        return False

"""
The tortoise and hare

TC: O(n)
SC: O(1)
""" 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
