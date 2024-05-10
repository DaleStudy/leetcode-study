# Time complexity : O(m*n)
# Space complexity : O(1)
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Create a dummy node to simplify the logic
        dummy = ListNode(None)
        # Pointer to the current node in the merged list
        node = dummy

        # Loop until both lists have nodes
        while list1 and list2:
            # Choose the smaller value between list1 and list2
            if list1.val < list2.val:
                # Append list1 node to the merged list
                node.next = list1
                # Move to the next node in list1
                list1 = list1.next
            else:
                # Append list2 node to the merged list
                node.next = list2
                # Move to the next node in list2
                list2 = list2.next
            # Move to the next node in the merged list
            node = node.next

        # Append the remaining nodes from list1 or list2
        node.next = list1 or list2

        # Return the merged list (skip the dummy node)
        return dummy.next
