from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        - Idea: 두 포인터(slow, fast)를 사용하여 slow가 삭제할 노드의 이전 노드에 위치하도록 한다.
            slow.next를 조정하여 삭제할 노드를 건너뛰도록 한다.
            삭제할 노드가 head일 경우를 간단히 처리하기 위해 dummy 노드를 사용한다.
        - Time Complexity: O(n). n은 리스트의 노드 수.
            최대 전체 리스트를 순회하여 삭제할 노드를 찾고 제거하므로 O(n)이 소요된다.
        - Space Complexity: O(1).
            dummy 노드와 slow, fast 포인터를 위한 상수 공간만 필요하다.
        """

        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
