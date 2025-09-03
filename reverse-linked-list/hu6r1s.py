# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  """
  링크드 리스트 학습을 따로 해야할 필요성이 있음
  """
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    stack = []
    node = head
    while node:
        stack.append(node)
        node = node.next
    
    dummy = ListNode()
    output = dummy
    while stack:
        output.next = stack.pop()
        output = output.next

    output.next = None
    return dummy.next
