# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        merged_list = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                merged_list.next = list1
                list1 = list1.next
            else:
                merged_list.next = list2
                list2 = list2.next
            # merged_list 포인터를 한칸 이동시켜서 다음 노드 붙일 준비
            merged_list = merged_list.next

        # 남아 있는 노드 붙이기
        merged_list.next = list1 if list1 is not None else list2

        return dummy.next
