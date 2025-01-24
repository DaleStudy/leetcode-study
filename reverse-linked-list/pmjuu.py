'''
시간 복잡도: O(n)
- 리스트의 모든 노드를 한 번씩 방문하므로 시간 복잡도는 O(n)입니다.

공간 복잡도: O(n)
- 재귀 호출을 사용하므로 호출 스택에 최대 n번의 함수 호출이 쌓이므로 공간 복잡도는 O(n)입니다.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)  # find the last node
        head.next.next = head                   # reverse
        head.next = None                        # remove cycle

        return new_head
