"""
# Intuition
-
# Approach
-
# Complexity
time : O(N+M)
space : O(1) / O(N+M)
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(None)  # -> None(고정)
        node = dummy  # -> None(이동)

        while list1 and list2:

            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            node = node.next  # (이동)

        # 반복문 종료
        node.next = list1 or list2

        return dummy.next  # 병합 리스트의 첫 번째 노드를 가리킴


# list1: 1 -> 2 -> 4
list1_node3 = ListNode(4)
list1_node2 = ListNode(2, list1_node3)
list1_node1 = ListNode(1, list1_node2)

# list2: 1 -> 3 -> 4
list2_node3 = ListNode(4)
list2_node2 = ListNode(3, list2_node3)
list2_node1 = ListNode(1, list2_node2)

sol = Solution()
merged_list = sol.mergeTwoLists(list1_node1, list2_node1)

# 결과 출력
current = merged_list
result = []
while current:
    result.append(current.val)
    current = current.next

print(result)


""" 재귀
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # 기저조건
        if not (list1 and list2):
            return list1 or list2

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
"""
