# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
# 141. Linked List Cycle

1. Create an empty list to keep track of visited nodes.
2. Traverse the linked list starting from the head node.    

'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: 
        record = []
        if head == None:
            return False 

        while head.next:
            record.append(head)
            if head.next in record:
                return True 
            head = head.next 
        return False 
