from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        - Idea: 사이클이 있는 연결 리스트인지 판단하기 위해 두 개의 포인터, slow와 fast를 사용한다.
            slow 포인터는 한번에 한 칸씩, fast 포인터는 한번에 두 칸씩 이동한다.
            만약 두 포인터가 만나면, 리스트에 사이클이 존재한다고 판단할 수 있다.
            fast가 리스트의 끝에 도달한다면 사이클이 없다고 판단한다.
        - Time Complexity: O(n). n은 리스트에 포함된 노드의 개수다.
            사이클이 없는 경우, fast 포인터는 리스트 끝까지 이동한다.
            사이클이 있는 경우, 두 포인터가 만날 때까지 이동하므로 O(n)의 시간이 소요된다.
        - Space Complexity: O(1). 연결 리스트의 크기와 상관없이 slow와 fast 변수만 사용되므로
            상수 공간만 차지한다.
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
