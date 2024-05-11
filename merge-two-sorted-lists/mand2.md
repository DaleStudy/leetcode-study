### Intuition

### Approach

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
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        merged_list = ListNode()
        current = merged_list

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
        
            current = current.next # pointer setting.

        current.next = l1 if l1 else l2

        return merged_list.next
```
