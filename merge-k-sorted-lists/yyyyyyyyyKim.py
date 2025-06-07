# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 분할정복(divide and conquer), 쉽지않음,다시볼것,다른방식풀이들찾아볼것.
        
        # 빈 리스트일 경우 None 반환
        if len(lists) == 0:
            return None

        # 두 개의 리스트 병합하는 함수
        def merge(list1, list2):
            dummy = ListNode()  # 시작노드
            tail = dummy        # dummy의 끝을 가리키는 포인터

            # list1와 list2에 노드가 있을 동안 반복
            while list1 and list2:
                # list1값과 list2값 중 더 작은 노드 값을 dummy에 추가
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            
            # 남은 노드들 붙이기
            if list1:
                tail.next = list1
            if list2:
                tail.next = list2

            # dummy의 다음이 병합 결과
            return dummy.next

        # 전체 리스트가 하나가 될 때까지 병합
        while len(lists) > 1:
            merged = []
            
            # 리스트 두 개씩 병합하기
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                
                if i + 1 < len(lists):
                    list2 = lists[i+1]
                else:
                    list2 = None
                
                merged.append(merge(list1,list2))

            # 병합된 리스트로 업데이트
            lists = merged

        # 하나로 병합된 리스트 반환
        return lists[0]
