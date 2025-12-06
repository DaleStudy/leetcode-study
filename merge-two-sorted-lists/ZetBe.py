'''
문제: 두 개의 정렬된 연결 리스트를 병합하여 하나의 정렬된 연결 리스트를 만드시오.
풀이: 두 연결 리스트의 노드를 비교하면서 작은 값을 가진 노드를 결과 리스트에 추가하는 방식으로 병합합니다.
시간 복잡도: O(n + m), n과 m은 각각 두 연결 리스트의 길이입니다. 두 리스트의 모든 노드를 한 번씩 방문하므로 전체 시간 복잡도는 O(n + m)입니다.
공간 복잡도: O(1), 추가적인 연결 리스트를 생성하지 않고 기존 노드들을 재사용하므로 공간 복잡도는 O(1)입니다.
사용한 자료구조: 연결 리스트
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list2 == None:
            return list1
        if list1 == None:
            return list2
        
        if list1.val <= list2.val:
            a, b = list1, list2
        else:
            b, a = list1, list2
        # 얕은 복사 활용 (중요해보임)
        result = a
        while a != None and b != None:
            if a.next != None and a.val <= b.val and a.next.val <= b.val:
                a = a.next
            else:
                a.next, b = b, a.next
                a = a.next
        return result


