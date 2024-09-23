
#  Runtime: 39ms, Memory: 17.88MB
#  Time complexity: O(len(head))
#  Space complexity: O(len(head))


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.nodes = []  # ListNode 객체를 저장할 배열

    def reverseList(self, head: Optional[ListNode]) -> List[Optional[ListNode]]:
        prev = None
        curr = head

        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
    
        return prev
