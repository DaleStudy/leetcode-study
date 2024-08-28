# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    TC: O(n) in worst case
    SC: O(n) in worst case
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        current_node = root

        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left

            current_node = stack.pop()
            n += 1
            if n == k:
                return current_node.val
            current_node = current_node.right
