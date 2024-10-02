from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        - Idea: dummy node를 하나 만들고, 두 리스트를 순회하면서 값을 비교하여 더 작은 노드를 dummy node에 이어 붙인다.
          둘 중 하나가 먼저 순회가 끝났다면, 나머지 리스트의 남은 노드들을 그대로 이어 붙인다. (리스트 내에서는 순서가 정렬되어 있음이 보장되어 있기 때문에 가능하다.)
        - Time Complexity: O(n), n은 m + k, m과 k은 각각 list1, list2의 길이이다.
        - Space Complexity: O(1), 추가적인 공간은 사용하지 않고, 기존 노드를 재사용하여 연결한다.
        """
        merged = ListNode()
        cur = merged

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next

        cur.next = list1 or list2

        return merged.next
