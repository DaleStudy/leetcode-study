# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        

        def go(cur: TreeNode) -> Optional[TreeNode]:
            if not cur:
                return cur
            res = TreeNode(cur.val)
            res.left = go(cur.right)
            res.right = go(cur.left)
            return res

        return go(root)
