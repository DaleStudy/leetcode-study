# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return

        if sum([1 if node is None else 0 for node in lists]) == len(lists):
            return

        def find_min():
            idx = -1
            min_val = sys.maxsize
            i = 0
            for l in lists:
                if l is not None and min_val > l.val:
                    min_val = l.val
                    idx = i
                i += 1

            return idx

        idx = find_min()
        node = lists[idx]
        head = node
        lists[idx] = lists[idx].next
        while node:
            idx = find_min()
            if idx == -1:
                break
            node.next = lists[idx]
            node = node.next
            lists[idx] = lists[idx].next

        return head
