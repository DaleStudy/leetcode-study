# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # 투포인터
        # 시간복잡도 O(n), 공간복잡도 O(1)

        # 더미 노드 사용(head삭제되는경우대비)
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        # fast를 n칸 이동(slow와의 간격n으로 유지)
        for _ in range(n):
            fast = fast.next

        # fast가 끝에 도달할때까지 slow와 한 칸씩 이동
        while fast.next:
            fast = fast.next
            slow = slow.next

        # slow.next = 삭제대상, 건너뛰고연결(삭제처리)
        slow.next = slow.next.next

        # 새로운 head 반환
        return dummy.next
