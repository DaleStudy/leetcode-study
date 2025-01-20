"""
Constraints:
- The number of nodes in the list is the range [0, 5000]
- -5000 <= Node.val <= 5000

Time Complexity: O(n)
- n은 linked list의 노드 수
- 리스트를 한 번 순회하면서 각 노드를 한 번씩만 방문하기 때문

Space Complexity: O(1)
- 추가 공간으로 prev, curr, temp 세 개의 포인터만 사용
- 입력 크기와 관계없이 일정한 추가 공간만 사용

풀이 방법:
1. 세 개의 포인터를 사용하여 리스트를 순회하면서 뒤집기
   - prev: 이전 노드를 가리키는 포인터
   - curr: 현재 노드를 가리키는 포인터
   - temp: 다음 노드를 임시 저장하는 포인터

2. 각 단계에서:
   - 다음 노드 임시 저장 (temp)
   - 현재 노드의 next를 이전 노드로 변경
   - 포인터들을 한 칸씩 전진

3. 참고:
   - 포인터들의 이동 순서가 중요
   - prev가 새로운 head가 됨
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
