from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        - Idea:
            연결 리스트를 반으로 나누고, 뒤쪽(두번째 리스트)의 연결 방향을 반대로 뒤집는다.
            첫번째 리스트와 두번째 리스트의 노드를 번갈아가며 연결한다.
        - Time Complexity: O(n). n은 전체 노드의 수
            리스트를 탐색하고 병합하는 데 걸리는 시간에 비례한다.
        - Space Complexity: O(1)
            몇 개의 포인터를 사용하는 상수 공간만 차지한다.
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        prev, cur = None, mid

        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp

        first, second = head, prev

        while second:
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            first, second = first_next, second_next
