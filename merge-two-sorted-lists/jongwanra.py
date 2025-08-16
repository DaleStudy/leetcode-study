"""
[Problem]
https://leetcode.com/problems/merge-two-sorted-lists/description/

두 정렬된 링크드 리스트의 Head가 주어진다.
두 리스트를 하나의 정렬된 리스트로 합치시오.
merged linked list의 Head를 반환하자.

[Brainstorming]
두 개의 Sorted Linked Listd의 Head가 주어졌을 떄, 이미 정렬이 되어 있기 떄문에
반복문을 총 2번 순회하여 하나의 Merged Linked List를 만들 수 있다.

[Complexity]
N: list1.length, M: list2.length
Time: O(N + M)
Space: O(N + M)

[Todo]
- 재귀적으로 풀어보기.

"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current_node = dummy_head
        while list1 and list2:
            if list1.val > list2.val:
                current_node.next = ListNode(list2.val)
                list2 = list2.next
            else:
                current_node.next = ListNode(list1.val)
                list1 = list1.next
            current_node = current_node.next

        current_node.next = list1 or list2

        return dummy_head.next


def generate(list:List[int])->Optional[ListNode]:
    dummy_head = ListNode(0)
    current_node = dummy_head
    for x in list:
        current_node.next = ListNode(x)
        current_node = current_node.next
    return dummy_head.next

def print_list(node:Optional[ListNode])->None:
    list = []
    while node:
        list.append(node.val)
        node = node.next
    print(list)

sol = Solution()
print_list(sol.mergeTwoLists(generate([1,2,4]), generate([1,3,4])))


