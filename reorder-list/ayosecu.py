from typing import Optional
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        - Time Complexity: O(N), N = The number of nodes.
        - Space Complexity: O(N)
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        dq = deque()

        cur = head
        while cur:
            dq.append(cur)
            cur = cur.next
        
        dummy = ListNode(-1)
        cur = dummy
        flag = True
        while dq:
            if flag:
                cur.next = dq.popleft()
            else:
                cur.next = dq.pop()
            cur = cur.next
            flag = not flag
        cur.next = None

        return dummy.next

### TC Helpers ###
def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

### TC ###
tc = [
        ([1,2,3,4], [1,4,2,3]),
        ([1,2,3,4,5], [1,5,2,4,3])
]

sol = Solution()
for i, (l, e) in enumerate(tc, 1):
    r = linked_list_to_list(sol.reorderList(build_linked_list(l)))
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
