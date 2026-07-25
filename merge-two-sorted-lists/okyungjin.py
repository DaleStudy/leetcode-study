# list1의 노드 개수를 n, list2의 노드 개수를 m이라 할 때
# 시간 복잡도: O(n + m)
# 공간 복잡도: O(1) -> dummy만 사용, 추가 공간 복잡도는 O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy: 병합된 결과 리스트의 시작점을 보존하기 위한 가상의 헤드 노드
        # current: 현재 병합 위치를 추적하며 노드를 연결해 나가는 포인터
        dummy = ListNode(None)
        current = dummy
        
        # 두 리스트가 모두 존재하는 동안 값을 비교하며 merge한다
        while list1 and list2:
            # 더 작은 값을 가진 노드를 결과 리스트에 연결
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # 병합 리스트의 포인터를 다음으로 이동
            current = current.next
        
        # 한쪽 리스트가 소진되면 남은 노드들을 한 번에 연결
        current.next = list1 if list1 else list2
        
        # dummy 노드의 다음부터가 실제 정렬된 리스트의 시작
        return dummy.next
