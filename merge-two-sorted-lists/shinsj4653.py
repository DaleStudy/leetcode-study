"""
[문제풀이]
# Inputs
- two sorted linked lists
# Outputs
- 두 링크드 리스트를 합쳐서 하나의 정렬된 (오름차순) 리스트 반환
# Constraints
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
# Ideas
두 링크드 리스트는 모두 오름차순으로 정렬되어 있음
-> ListNode는 val, next 로 되어있음

우선 두 리스트 이어붙이고,
먼가 리스트 정렬 알고리즘 써야할듯?
리스트라서, 두 노드를 바꾸는 swap() 함수 쓰면서,
왼쪽보다 오른쪽이 작으면 바꾸는 식으로 하면 될듯?

즉, 붙어있는 두 노드 비교하면서 쭉 돌기
하지만 인덱스가 없어서 어떻게 순회할지?
-> point라는 기준을 둬서 이 point를 기준으로 prev, next를 만들어서 순회
-> 근데 prev, next만으로는 swap이 어려워서 2개가 아닌 3개를 둬야할 것 같은데,
구현 방법이 떠오르지 않아서 해설 참고

해설 참고
- 기존 리스트 변경이 아닌, 아예 새로운 리스트를 재창조 하는 방식으로!


[회고]
기존 리스트를 swap하려고 하다 보니, 어렵게 생각하게됨..

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        retList = ListNode(None)
        head = retList

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next

            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        head.next = list1 or list2
        return retList.next

