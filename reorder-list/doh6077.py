# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Time Complexity: O(N)
        # The order: 
        # 0, n, 1, n -1, 2, n-3 ...
        # first Idea
        # need to save the index of the original head 
        # Hashmap: iterate through the head until head it none, save index as key and head.val as value 
        head_hash = {}
        temp = head
        index = 0 
        length = 0 
        # Save index and value in the hashmap
        while temp is not None:
            head_hash[index] = temp.val
            temp = temp.next 
            index += 1
            length += 1
        # reset index to 0, and use it to iterate through the head again
        index = 0 
        # to keep track of n-1, n-2, n-3 ...
        count = 1
        # Iterate through the head again and change the value based on the index
        while head is not None: 
            res = index % 2 
            # if the index is even number 
            if res == 0:
                head.val = head_hash[index/2]
            # n, n-1, n-2 when the index is odd 
            else:
                head.val = head_hash[length - count]
                count += 1 
            index += 1
            head = head.next
