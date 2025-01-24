# TC:O(n), SC:O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prv = None
        while cur != None:
            tmp = cur.next # 다음 노드의 주소를 tmp에 저장
            cur.next = prv # 현재 노드가 가리키는 주소를 prv로 설정
            prv = cur # prv를 현재 노드로 설정
            cur = tmp # 현재 노드를 그 다음 노드로 변경
        return prv
