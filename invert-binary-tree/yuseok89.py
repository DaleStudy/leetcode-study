# TC: O(N)
# SC: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        else:
            cur_node = TreeNode(root.val)

            cur_node.right = self.invertTree(root.left)
            cur_node.left = self.invertTree(root.right)

            return cur_node

