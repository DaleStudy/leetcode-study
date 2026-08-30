"""
시간복잡도: O(n)
공간복잡도: O(1)

1. 토끼와 거북이 포인터를 이용해 연결 리스트의 중간 지점을 찾는다.
2. 중간 지점부터 끝까지의 리스트를 역순으로 뒤집는다.
   - 이 과정에서 앞부분과 뒷부분이 분리된다.
3. 앞부분(head)과 뒤집힌 뒷부분을 교차로 연결하여 순서를 재배열한다.
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tortoise = hare = head

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

        prev, curr = None, tortoise
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        a, b = head, prev
        while b.next:
            a.next, a = b, a.next
            b.next, b = a, b.next
