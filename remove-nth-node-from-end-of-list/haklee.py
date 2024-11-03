"""TC: O(n), SC: O(1)

n은 주어진 리스트의 길이.

아이디어:
- 길이를 먼저 측정한다.
- 그 다음 제거할 노드의 인덱스를 구해서 해당 인덱스의 아이템을 제거.

SC:
- 리스트의 길이 값 및 리스트 탐색에 사용하는 인덱스 값을 관리. O(1).

TC:
- 길이 값 구할때 리스트를 전체 순회. O(n).
- 특정 인덱스에 해당하는 노드 제거시 최악의 경우 끝 노드까지 탐색해야 한다. O(n).
- 종합하면 O(n).
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 길이 측정
        l = 0
        cur_head = head
        while True:
            if not cur_head:
                break
            l += 1
            cur_head = cur_head.next

        # 노드 하나 제거
        i = 0
        dummy_head = ListNode()
        dummy_head.next = head
        cur_head = dummy_head
        while i != l - n:
            i += 1
            cur_head = cur_head.next

        cur_head.next = None if cur_head.next is None else cur_head.next.next
        return dummy_head.next
