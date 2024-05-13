# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subroot):
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            if root.val != subroot.val:
                return False

            return dfs(root.left, subroot.left) and dfs(root.right, subroot.right)

        def solve(root, subroot):
            if not root:
                return False
            if dfs(root, subroot):
                return True
            return solve(root.left, subroot) or solve(root.right, subroot)

        return solve(root, subRoot)

        ## TC: O(mn), where m and n denote len(subroot) and len(root)
        ## SC: O(m+n)
