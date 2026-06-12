# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_same(node, subnode):
            if not node and not subnode:
                return True
            elif node and subnode:
        
                if node.val != subnode.val:
                    return False

                return (
                    check_same(node.left, subnode.left)
                    and check_same(node.right, subnode.right)
                )
            return False

        def dfs(node):
            if not node:
                return False

            if node.val == subRoot.val and check_same(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)
