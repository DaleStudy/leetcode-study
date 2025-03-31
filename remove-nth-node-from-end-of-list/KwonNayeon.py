"""
Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Time Complexity: O(n)
- 여기서 n은 리스트의 길이, 리스트를 한 번만 순회함

Space Complexity: O(1)
- 추가 공간을 사용하지 않음, 정해진 개수의 변수만 사용

풀이방법:
1. fast 포인터를 n번 앞으로 이동
2. base case: 만약 fast가 None이라면, 첫 번째 노드를 제거함
3. fast.next가 None일 때까지 두 포인터를 함께 이동
4. slow의 다음 노드를 제거함 (slow.next = slow.next.next로 연결을 끊어냄)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
