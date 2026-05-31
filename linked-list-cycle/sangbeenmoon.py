# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        MM = 10001
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            if cnt > MM:
                return True
            cur = cur.next
        
        return False
