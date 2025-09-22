# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  """
  생각보다 쉬운 문제.
  """
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    visited = set()
    while head:
      if head in visited:
        return True
      visited.add(head)
      head = head.next
    return False
