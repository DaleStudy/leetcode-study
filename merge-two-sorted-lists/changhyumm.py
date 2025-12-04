# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # head of merged linked list를 반환해야 하므로 head를 임시로 생성
        head = ListNode()
        pointer = head

        # 정렬된 링크드 리스트이므로 하나라도 끝까지 pointer를 이동해서 None이 될때까지 loop
        # 시간복잡도 O(n), 공간복잡도 O(1)
        while list1 and list2:
            # val 비교해서 next 지정
            if list1.val <= list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            # pointer도 next로 이동
            pointer = pointer.next
        # 남은 리스트의 경우 정렬되어 있으므로 그대로 연결
        if list1:
            pointer.next = list1
        else:
            pointer.next = list2

        return head.next
