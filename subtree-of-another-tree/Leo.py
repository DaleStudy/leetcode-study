# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False

            return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)

        def solve(root):
            if not root:
                return False
            if dfs(root, subRoot):
                return True
            return solve(root.left) or solve(root.right)

        return solve(root)

        ## TC: O(mn), where m and n denote len(subroot) and len(root)
        ## SC: O(m+n)
