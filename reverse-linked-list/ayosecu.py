from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        - Time Complexity: O(n), n = The number of nodes.
        - Space Complexity: O(1)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        
        return pre

def toLinkedList(lists):
    dummy = ListNode(-1)
    ptr = dummy
    for item in lists:
        ptr.next = ListNode(item)
        ptr = ptr.next
    return dummy.next

def toList(head):
    result = []
    
    while head:
        result.append(head.val)
        head = head.next
    
    return result

tc = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], [])
]

sol = Solution()
for i, (l, e) in enumerate(tc, 1):
    r = toList(sol.reverseList(toLinkedList(l)))
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
