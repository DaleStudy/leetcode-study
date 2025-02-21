"""
가장 뒤부터 돌아오는 방법을 찾아야한다.
1) 재귀 스택 방식
2) 새로운 리스트를 만드는 방법
3) two pointer 로 반 잘라서 reverse 한 뒤 merge
"""

"""
Solution: 3) Two pointer 
Time: O(n)
Space: O(1)
"""


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 절반 자르기
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
