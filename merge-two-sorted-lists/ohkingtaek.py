# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        시간복잡도: O(n)
        공간복잡도: O(1)
        1. 두 리스트를 합쳐서 새로운 리스트 반환
        2. 두 리스트를 돌면서 작은 값을 새로운 리스트에 추가
        3. 두 리스트를 모두 순회하면 남은 것을 새로운 리스트에 추가
        """
        root = ListNode(None)
        node = root
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return root.next
