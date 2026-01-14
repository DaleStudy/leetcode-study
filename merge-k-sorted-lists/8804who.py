import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for node in lists:
            if not node:
                continue
            while True:
                heapq.heappush(heap, node.val)
                node = node.next
                if not node:
                    break

        def makeNode():
            node = ListNode()
            if not heap:
                return None
            node.val = heapq.heappop(heap)
            node.next = makeNode()
            return node

        return makeNode()
    
