# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp =[]
        while head:
            temp.append(head.val)
            head = head.next

        temp = temp[::-1] #Reverse the temp list 
        
        myNode = ListNode() #Create the Listnode instance 
        current = myNode
        
        for value in temp:
            current.next = ListNode(value)
            current = current.next
        
        return myNode.next
