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
- 투 포인터 기법: 두 포인터 사이의 고정된 간격(n)을 이용하여 fast가 끝에 도달했을 때 slow가 정확한 위치에 있도록 함
1. fast 포인터를 n번 이동시켜 slow와 n칸 간격을 만듦
2. Base case: fast가 None이면 첫 번째 노드를 삭제 (head.next 반환)
3. fast.next가 None일 때까지 두 포인터를 함께 이동
   -> 이때 slow는 삭제할 노드의 바로 앞 위치에 도달
4. slow.next = slow.next.next로 삭제할 노드를 건너뛰도록 연결 변경
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
