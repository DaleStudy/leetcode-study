# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Time Complexity: O(N)
Space Complexity: O(1)

1. Create a dummy node to store the head of the merged list ( return_node )
2. Traverse the two lists until one of the lists is empty
3. Compare the values of the two nodes and add the smaller node to the dummy node
4. Move the pointer of the list with the smaller node to the next node
5. Add the remaining nodes of the non-empty list to the dummy node
6. Return the next node of the dummy node
"""
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        node = head

        while list1 and list2:
            if list1.val > list2.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next

            head = head.next

        head.next = list1 or list2

        return node.next

"""
Time Complexity: O(N)
Space Complexity: O(N) - Recursive stack space

1. If one of the lists is empty, return the other list
2. Compare the values of the two nodes and add the smaller node to the merged list
3. Move the pointer of the list with the smaller node to the next node
4. Return the next node of the merged list
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        if list1.val > list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
