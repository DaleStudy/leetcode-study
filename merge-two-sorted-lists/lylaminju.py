from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next

        current.next = list1 or list2

        return head.next
    
# 시간 복잡도:
# - 두 리스트의 모든 노드를 순회하며 병합하므로 O(n + m) => O(n) 으로 표현
#   여기서 n은 list1의 길이, m은 list2의 길이.
#
# 공간 복잡도:
# - 기존 노드를 재사용하므로 O(1)
