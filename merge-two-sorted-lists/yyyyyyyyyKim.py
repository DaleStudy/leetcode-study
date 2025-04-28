# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)    # 더미 시작 노드
        current = dummy         # 현재 연결 위치 포인터

        while list1 and list2:

            # 현재list1의 값과 현재list2값을 비교해서 current.next 연결
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # current 다음으로 이동
            current = current.next

        # 둘 중 하나가 남아있다면 나머지를 통째로 붙이기(삼항 연산자)
        current.next = list1 if list1 else list2
        # if list1:
        #     current.next = list1
        # else:
        #     current.next = list2
        
        return dummy.next
