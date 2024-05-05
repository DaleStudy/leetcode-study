# Time complexity : O(n)
# Space complexity : O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head

        while node:
            stack.append(node.val)
            node = node.next

        node = head
        while node:
            node.val = stack.pop()
            node = node.next

        return head
