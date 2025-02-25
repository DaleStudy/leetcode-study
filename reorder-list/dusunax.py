'''
# 143. Reorder list
use two pointers for each steps.

1. finding the middle
    - two pointers: slow, fast
    - move slow 1, fast 2 until fast reaches the end.
2. reversing the second half
    - two pointers: prev, curr
    - start from slow to end, do common reverse linked list operation.
    - need to break the links to halves beforehand.
3. merging first & second
    - two pointers: frist, second
    - merge second between first, until second is None

## TC is O(n)
- find the middle: O(n)
- reverse the second half: O(n)
- merge the two halves: O(n)

## SC is O(1)
- no extra space is used.
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. finding the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reversing second half
        second_not_reversed = slow.next
        slow.next = None
        prev, curr = None, second_not_reversed
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 3. merging first & second
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
