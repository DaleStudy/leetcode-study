"""
Solution:
    1) temp node를 저장합니다.
    2) cur node 를 prev node 로 연결시킵니다.
    3) cur node 가 prev node 가 됩니다.
    4) cur node 는 temp node 가 됩니다.
Time: O(n)
Space: O(1)
"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
