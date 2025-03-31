'''
시간 복잡도: O(n)
- `fast`와 `slow` 포인터가 리스트를 한 번 순회하면서 주어진 연결 리스트의 길이에 비례하는 작업을 수행합니다.
- 따라서 최악의 경우 모든 노드를 한 번씩 방문하게 되므로 O(n)입니다.

공간 복잡도: O(1)
- 추가적인 자료구조를 사용하지 않고, `fast`와 `slow`라는 두 개의 포인터만 사용하므로 O(1)입니다.
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        
        return False
