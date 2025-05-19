from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        - Time Complexity: O(n + m), n = len(list1), m = len(list2)
        - Space Complexity: O(1)
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers
        p1, p2 = list1, list2
        dummy = ListNode(0)
        current = dummy
        
        while p1 and p2:  
            if p1.val < p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        
        current.next = p1 if p1 else p2
        
        return dummy.next

def printList(list):
    if not list:
        print("[]")
        return
    
    str_list = []
    while list:
        str_list.append(str(list.val))
        list = list.next
    print("[" + ", ".join(str_list) + "]")

def doTest():
    sol = Solution()

    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    result1 = sol.mergeTwoLists(list1, list2)
    printList(result1)

    result2 = sol.mergeTwoLists(None, None)
    printList(result2)

    result3 = sol.mergeTwoLists(None, ListNode(0))
    printList(result3)

doTest()
