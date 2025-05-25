# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle_on(self, head: Optional[ListNode]) -> bool:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)

        [Approach]
            hash table로 visited 노드를 기록한다.
        """
        curr = head
        visited = set()

        while curr:
            if curr in visited:
                return True

            visited.add(curr)
            curr = curr.next

        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            Floyd’s Cycle Detection 알고리즘을 사용한다.
            linked list에서 slow (1칸씩 전진) & fast (2칸씩 전진) runner를 이용하면,
                - slow와 fast가 만난다면 cyclic
                - 만나지 않은 채로 fast가 끝에 도달하면 not cyclic
            이다.
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
