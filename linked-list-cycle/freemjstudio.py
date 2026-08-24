# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        flag = False
        visited = set()

        node = head

        while node is not None:

            if node not in visited:
                visited.add(node)
            else:
                flag = True
                break
            # move to the next node
            node = node.next

        return flag
