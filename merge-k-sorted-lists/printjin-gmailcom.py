from typing import List, Optional
class Solution:
    def mergeKLists(self, lists)]:
        values = []
        for l in lists:
            while l:
                values.append(l.val)
                l = l.next
        values.sort()
        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
