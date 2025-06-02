from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
        - Time Complexity: O(n), n = The number of nodes
        - Space Complexity: O(1)
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow, fast = head, head
        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False

            if fast == slow:
                return True
            
        return False

# Run Test Cases
def do_test():
    sol = Solution()

    h1 = ListNode(3)
    h1.next = ListNode(2)
    h1.next.next = ListNode(0)
    h1.next.next = ListNode(-4)
    h1.next.next.next = h1.next
    r1 = sol.hasCycle(h1)
    print(f"TC 1 is Passed!" if r1 == True else f"TC 1 is Failed!")

    h2 = ListNode(1)
    h2.next = ListNode(2)
    h2.next.next = h2
    r2 = sol.hasCycle(h2)
    print(f"TC 2 is Passed!" if r2 == True else f"TC 2 is Failed!")

    h3 = ListNode(1)
    r3 = sol.hasCycle(h3)
    print(f"TC 3 is Passed!" if r3 == False else f"TC 3 is Failed!")

do_test()
