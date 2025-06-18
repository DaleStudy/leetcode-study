# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd_recur(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        [Complexity]
            - TC: O(len)
            - SC: O(len) (call stack)

        [Approach]
            재귀적으로 linked list를 확인하며 끝에서부터의 순서를 확인 후, 다음 node의 순서가 n과 같을 때 다음 node를 건너뛰도록 한다.
            head node를 제거해야 하는 경우(= 끝에서부터 n번째인 node가 head인 경우)에는, 재귀 함수 내에서 node 제거가 불가능하므로 head.next를 반환한다.
        """

        def check_order_from_end(curr):
            # base condition
            if not curr.next:
                return 1

            # recur
            next_order_from_end = check_order_from_end(curr.next)
            # nth from end인 node를 건너뛰기
            if next_order_from_end == n:
                curr.next = curr.next.next

            return next_order_from_end + 1

        # head node를 제거해야 하는 경우라면, check_order_from_end() 내에서 node 제거가 불가능하므로 head.next를 반환해야 함
        if check_order_from_end(head) == n:
            return head.next

        return head

    def removeNthFromEnd_recur2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        [Complexity]
            - TC: O(len)
            - SC: O(len) (call stack)

        [Approach]
            이전 풀이에서 head node를 제거해야 하는 경우를 따로 처리하지 않으려면, 주어진 head를 가리키는 dummy node(= prev)를 추가하고
            dummy node의 next node를 반환하면 된다.
        """

        def check_order_from_end(curr):
            # base condition
            if not curr.next:
                return 1

            # recur
            next_order_from_end = check_order_from_end(curr.next)
            # nth from end인 node를 건너뛰기
            if next_order_from_end == n:
                curr.next = curr.next.next

            return next_order_from_end + 1

        prev = ListNode(next=head)
        check_order_from_end(prev)

        return prev.next

    def removeNthFromEnd_length(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            linked list의 전체 길이를 구하고, head에서부터 (길이 - n - 1) 번 전진하여 node를 건너뛰면 된다.
            (2 pass)
        """
        # linked list의 length 구하기
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # length == n라면, head를 제거
        if length == n:
            return head.next

        # length - n - 1 번 이동
        curr = head
        for _ in range(length - n - 1):
            curr = curr.next

        # node 제거
        curr.next = curr.next.next

        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        [Complexity]
            - TC: O(len)
            - SC: O(1)

        [Approach]
            slow, fast의 two pointer를 이용해 반복문으로 풀 수 있다. (1 pass)
                1. fast를 n 번 전진
                2. fast가 끝에 도달한 경우, 첫 번째 node를 제거해야하므로 head.next 반환
                3. 현재 fast의 위치에서 slow와 fast를 함께 전진하면, fast가 끝에 도달할 때 slow는 뒤에서부터 n + 1번째 node임
                4. 뒤에서부터 n + 1번째인 node가 n - 1번째 node를 가리키도록 함
        """
        slow = fast = head

        # 1. fast를 n 번 전진
        for _ in range(n):
            fast = fast.next

        # 2. fast가 끝에 도달한 경우, 첫 번째 node를 제거해야하므로 head.next 반환
        if not fast:
            return head.next

        # 3. 현재 fast의 위치에서 slow와 fast를 함께 전진하면,
        #    fast가 끝에 도달할 때 slow는 뒤에서부터 n + 1번째 node임
        while fast.next:
            slow, fast = slow.next, fast.next

        # 4. 뒤에서부터 n + 1번째인 node가 n - 1번째 node를 가리키도록 함
        slow.next = slow.next.next

        return head
