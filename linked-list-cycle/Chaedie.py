"""
Solution:
    1) 사이클이 있다면 무한 루프가 발생할것이다.
    2) 사이클이 없다면 언젠가 null 이 될것이다.
    3) 따라서 두개의 포인터를 사용하여 동일한 Node에 도달하는 지 확인한다.
    4) null 이 된다면 사이클이 없다는 뜻이다.
Time: O(n)
Space: O(1)
"""


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
