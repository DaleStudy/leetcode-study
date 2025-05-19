# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList_iter(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            linked-list를 reverse 할 때의 핵심은
                (1) p1 -> p2를 p1 <- p2로 바꾸고
                (2) p1, p2를 모두 한 칸 앞으로 전진
            하는 것이다.
            이때, (1)에서 p2.next = p1로 바꾼다면, p2를 한 칸 앞으로 전진할 수 없기 때문에 먼저 p2.next(= p3)를 기록해둬야 한다.
            이를 iterative 하게 구현하면 while문을 이용할 수 있다.
        """
        p1, p2 = None, head

        while p2:
            # 1. p3 얻어놓기
            p3 = p2.next

            # 2. p1 <- p2 전환
            p2.next = p1

            # 3. p1 -> p2, p2 -> p3 이동
            p1, p2 = p2, p3

        return p1

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n) (call stack)

        [Approach]
            linked-list를 reverse 할 때의 핵심은
                (1) p1 -> p2를 p1 <- p2로 바꾸고
                (2) p1, p2를 모두 한 칸 앞으로 전진
            하는 것이다.
            이때, (1)에서 p2.next = p1로 바꾼다면, p2를 한 칸 앞으로 전진할 수 없기 때문에 먼저 p2.next(= p3)를 기록해둬야 한다.
            이를 recursive 하게 구현하려면 다음과 같이 base condition으로 종료조건을 추가해주면 된다.
        """

        def reverse_ll(p1, p2):
            # base condition
            if not p2:
                return p1

            # recur
            # 1. p3 얻어놓기
            p3 = p2.next

            # 2. p1 <- p2 전환
            p2.next = p1

            # 3. p1 -> p2, p2 -> p3 이동
            return reverse_ll(p2, p3)

        return reverse_ll(None, head)
