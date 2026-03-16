# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        checking validation using inorder traversal
        always greater than previous node's key

        time complexity: O(n)

        """

        prev = [None]

        def inorder(node):
            if not node:
                return True

            #search left sub tree first
            if not inorder(node.left):
                return False
            
            if prev[0] is not None and node.val <= prev[0]:
                return False

            #set current node value
            prev[0] = node.val
            #search right sub tree
            return inorder(node.right)

        return inorder(root)
