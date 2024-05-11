### Intuition
- 투 포인터 (prev, curr)

### Approach
- 투 포인터
- 포인터를 이동하기 전에 prev 가 가리키는 (.next) 를 reverse 해 주어야 한다.

### Complexity
- Time complexity: O(n)
- Space complexity: O(1)


### Code

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev, curr = None, head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
        
```
