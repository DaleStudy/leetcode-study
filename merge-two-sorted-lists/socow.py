"""
        문제 요약
        - 정렬된 두 연결 리스트를 하나의 정렬된 리스트로 병합

        아이디어
        - dummy 노드로 시작점 고정
        - 두 리스트 비교하며 작은 값을 연결
        - 남은 리스트 한번에 연결

        시간복잡도: O(n + m) - 두 리스트 길이의 합
        공간복잡도: O(1) - 추가 공간 없이 포인터만 변경
"""


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()  # 가짜 시작 노드
        node = dummy

        # 두 리스트 비교하며 병합
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        # 남은 리스트 연결
        node.next = list1 or list2

        return dummy.next
