# Time: O(N logN)
# Space: O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 :
            return None
        vals = []
        for node in lists:
            while node is not None:
                vals.append(node.val)
                node = node.next
        vals = sorted(vals)
        dummy = ListNode()
        curr = dummy

        for val in vals:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next

"""
# Time: O(kN)
# Space: O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 :
            return None
        dummy = ListNode()
        curr = dummy
        cache_val = [node.val if node is not None else float("inf") for node in lists ]

        while min(cache_val) != float("inf"):
            min_val = min(cache_val)
            min_idx = cache_val.index(min_val)

            curr.next = ListNode(min_val)
            curr = curr.next

            lists[min_idx] = lists[min_idx].next
            if lists[min_idx] is not None:
                cache_val[min_idx] = lists[min_idx].val
            else:
                cache_val[min_idx] = float('inf')

        return dummy.next
"""
