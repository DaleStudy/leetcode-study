from typing import List, Optional
from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        - Time Complexity: O(nlogk)
            - n = Total number of nodes in lists
            - k = The number of linked lists = len(lists)
        - Space Complexity: O(k)
            - Heap stores at most k elements at any time
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        tail = dummy
        
        while heap:
            val, i, node = heappop(heap)
            tail.next = node
            tail = node
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next

### TC Helpers ###
def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

### DO TEST ###
def do_test():
    sol = Solution()

    # TC 1
    lists = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6])
    ]
    e = [1, 1, 2, 3, 4, 4, 5, 6]
    merged = sol.mergeKLists(lists)
    r = linked_list_to_list(merged)
    print(f"TC 1 is Passed!" if r == e else f"TC 1 is Failed! - Expected: {e}, Result: {r}")

    # TC 2
    lists = [
        build_linked_list([]),
        build_linked_list([1]),
        build_linked_list([])
    ]
    e = [1]
    merged = sol.mergeKLists(lists)
    r = linked_list_to_list(merged)
    print(f"TC 2 is Passed!" if r == e else f"TC 2 is Failed! - Expected: {e}, Result: {r}")

    # TC 3
    lists = []
    e = []
    merged = sol.mergeKLists(lists)
    r = linked_list_to_list(merged)
    print(f"TC 3 is Passed!" if r == e else f"TC 3 is Failed! - Expected: {e}, Result: {r}")

do_test()
