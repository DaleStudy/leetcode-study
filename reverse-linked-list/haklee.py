"""TC: O(n), SC: O(1)

아이디어:
첫 아이템부터 차례대로 next로 넘어가면서 직전에 보았던 노드를 next에 넣어준다.

SC:
- 직전 노드를 관리한다. O(1).

TC:
- 모든 노드에 대해 직전 노드를 next에 대입한다.
- 그 외에 다른 연산도 O(1). 코드 참조.
- 종합하면 O(n).
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            next = cur.next
            cur.next = prev
            prev, cur = cur, next
        return prev
