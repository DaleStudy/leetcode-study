class Solution:
    # 시간복잡도: O(NlogK) N: 모든 리스트의 노드 수 합 K: 리스트의 개수
    # 공간복잡도: O(1) 기존 노드 재활용
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        if len(lists) == 1: return lists[0]

        def merge(a, b):
            res = ListNode()
            cur = res

            while a and b:
                if a.val > b.val:
                    cur.next = b
                    b = b.next
                else:
                    cur.next = a
                    a = a.next
                cur = cur.next

            if a:
                cur.next = a
            else:
                cur.next = b

            return res.next

        def mergeK(lo, hi):
            if lo == hi:
                return lists[lo]

            if hi - lo == 1:
                return merge(lists[lo], lists[hi])

            mid = (lo + hi) // 2
            left = mergeK(lo, mid)
            right = mergeK(mid+1, hi)

            return merge(left, right)

        return mergeK(0, len(lists)-1)
