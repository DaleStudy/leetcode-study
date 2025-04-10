class Solution:
    def isValidBST(self, root):
        prev = None
        def inorder(node):
            nonlocal prev
            if not node:
                return True
            if not inorder(node.left):
                return False
            if prev is not None and node.val <= prev:
                return False
            prev = node.val
            return inorder(node.right)
        return inorder(root)
