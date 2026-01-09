# idea : -
# Time complxity : O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            else:
                visited.add(head)
                head = head.next
        return False

# Floyd (cycle detection)
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         slow, fast = head, head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False

