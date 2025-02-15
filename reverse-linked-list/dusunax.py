'''
# 206. Reverse Linked List

iterate through the linked list and reverse the direction of the pointers.

## Time and Space Complexity

```
TC: O(n)
SC: O(1)
```
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current is not None: # TC: O(n)
            next_list_temp = current.next
            current.next = prev
            prev = current
            current = next_list_temp

        return prev
