# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        - TC: O(m+n)
        - SC: O(1)
        """

        # 엣지 케이스
        # 두 리스트 중 하나라도 비어 있는 경우,
        # 나머지 리스트 바로 반환
        if not list1:
            return list2
        if not list2:
            return list1
        
        # 더미 헤드 노드
        # 결과 리스트 시작점 역할을 할 가짜 노드 생성
        dummy = ListNode()
        current = dummy # current는 현재까지 만든 리스트의 마지막 노드

        # 두 리스트 모두 노드가 남아 있을 때까지 반복
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # 남은 노드들 이어 붙이기
        # 아직 노드가 남아 있는 리스트가 있으면 통째로 붙이기
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next
