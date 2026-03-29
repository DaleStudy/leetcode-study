# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        """두개의 링크드 리스트를 합쳐서 하나의 sorted 링크드 리스트를 만드는 함수

        방법:
        1. 각각의 리스트 head에서 값을 비교하면서,
            1번보다 2번의 값이 작으면 1번의 head를 움직이고,
            반대의 경우 2번의 head를 움직이도록 함.
            움직이면서 합치는 리스트에 tail.next로 붙여줌

        Args:
            list1 (ListNode | None): 정렬된 양수 링크드 리스트
            list2 (ListNode | None): 정렬된 양수 링크드 리스트 2

        Returns:
            ListNode | None: 하나로 합쳐진 정렬된 링크드 리스트
        """
        final = ListNode()
        tail = final
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        tail.next = curr1 if curr1 else curr2
        return final.next
