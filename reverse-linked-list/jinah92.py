# 복잡도
# 시간 복잡도: 링크드 리스트의 길이 N만큼 순회하는데 O(N)을, 다음 링크드 리스트를 검색하는 데 O(1)을 소요하므로 O(N)*O(1) = O(N)
# 공간 복잡도: 리턴할 dummy에 대해서만 메모리를 사용하므로 O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None # reversed linked list를 저장할 변수
        
        while head: # 노드 끝까지 순회
            current = head # 현재 노드의 복사본
            head = head.next # 다음 노드로 이동
            current.next = dummy # 복사본의 next의 방향을 역전
            dummy = current # 현재노드를 dummy head으로 변경
        
        return dummy
