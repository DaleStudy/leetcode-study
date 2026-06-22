"""
Time Complexity: O(n)
Space Complexity: O(1)

과정:
1. 두 개의 포인터를 사용하여 리스트를 순회하면서 뒤집음
2. 첫 번째 포인터는 이전 노드를 가리키고, 두 번째 포인터는 현재 노드를 가리킴
3. 현재 노드의 next를 이전 노드로 변경하고, 두 포인터를 한 칸씩 이동시킴
4. 마지막 노드까지 반복하면 리스트가 뒤집어짐
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left, now = None, head
        while now:
            right = now.next
            now.next = left
            left, now = now, right
        return left
