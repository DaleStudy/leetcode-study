from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.q = deque()

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head

        while temp:
            self.q.append(temp.val)
            temp = temp.next
        
        self.makeList(head, 0)

    def makeList(self, node, n):
        if n == 0:
            node.val = self.q.popleft()
        else:
            node.val = self.q.pop()
        if self.q:
            self.makeList(node.next, (n+1)%2)
    
