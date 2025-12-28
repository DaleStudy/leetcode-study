'''
Linked List의 노드는 value와 next 포인터를 가지고 있다는 특성을 이용해 문제를 풀었음

Time Complexity: O(n)
- Linked List의 모든 노드를 한 번씩 방문

Space Complexity: O(1)
- 두개 의 포인터만 사용하여 추가적인 공간 없음

'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev
