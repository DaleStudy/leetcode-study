# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 시간복잡도 O(n), 공간복잡도 O(1)
        answer = None

        while head:
            next_node = head.next   # 다음 노드 저장
            head.next = answer      # 현재 노드의 next를 이전 노드로 변경
            answer = head           # answer를 현재 노드로 업데이트
            head = next_node        # head를 다음 노드로 이동

        # answer = 역순 리스트의 head
        return answer
