"""
# Intuition
각각의 리스트의 첫 노드를 가리키면서 병합 리스트를 생성한다.

# Complexity
- Time complexity: list1과 list2의 길이 N, M일때 O(N+M)

- Space complexity: 기존 노드 연결만 바꿈 O(1)
"""


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # 남은 쪽 붙이기
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
