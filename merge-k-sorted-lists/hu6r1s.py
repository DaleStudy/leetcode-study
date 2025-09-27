# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    """
    브루트포스
    """
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     dummy = curr = ListNode()
    #     while any(lists):
    #         val, idx = min((li.val, idx) for idx, li in enumerate(lists) if li)
    #         curr.next = ListNode(val)
    #         curr = curr.next
    #         lists[idx] = lists[idx].next
    #     return dummy.next

    """
    최소힙 활용
    """
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     heap = [(li.val, idx) for idx, li in enumerate(lists) if li]
    #     heapq.heapify(heap)

    #     dummy = curr = ListNode()
    #     while heap:
    #         val, idx = heapq.heappop(heap)
    #         curr.next = ListNode(val)
    #         curr = curr.next

    #         lists[idx] = lists[idx].next
    #         if lists[idx]:
    #             heapq.heappush(heap, (lists[idx].val, idx))
    #     return dummy.next

    """
    분할정복과 재귀 활용
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(li1, li2):
            dummy = node = ListNode(-1)
            while li1 and li2:
                if li1.val < li2.val:
                    node.next = li1
                    li1 = li1.next
                else:
                    node.next = li2
                    li2 = li2.next
                node = node.next
            node.next = li1 if li1 else li2
            return dummy.next

        if len(lists) == 0:
            return None

        def dfs(low, high):
            if low == high:
                return lists[low]
            if low + 1 == high:
                return mergeTwoLists(lists[low], lists[high])

            mid = (low + high) // 2
            li1 = dfs(low, mid)
            li2 = dfs(mid + 1, high)
            return mergeTwoLists(li1, li2)

        return dfs(0, len(lists) - 1)
