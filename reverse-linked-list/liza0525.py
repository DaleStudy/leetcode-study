class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_node, curr_node = None, head
        while curr_node:
            temp = curr_node.next
            curr_node.next = pre_node
            pre_node, curr_node = curr_node, temp
        return pre_node
