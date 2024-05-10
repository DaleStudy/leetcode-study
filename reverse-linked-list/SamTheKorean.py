# Time complexity : O(n)
# Space complexity : O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Return None when head is None
        if not head:
            return None

        stack = []
        node = head

        while node:
            stack.append(node)
            node = node.next

        head = stack.pop()
        node = head

        # End the loop when stack is empty
        while stack:
            node.next = stack.pop()
            node = node.next

        # Set the last node's next to None to indicate the end of the reversed list
        node.next = None

        return head
