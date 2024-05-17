# TC: O(mn), SC: O(m+n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def prev(root, subRoot):
            if not root or not subRoot:
                return root == subRoot
            if root.val != subRoot.val:
                return False

            return prev(root.left, subRoot.left) and prev(root.right, subRoot.right)

        if not root:
            return False
        if prev(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
