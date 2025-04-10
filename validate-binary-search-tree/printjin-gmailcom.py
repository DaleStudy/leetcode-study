class Solution:
    def isValidBST(self, root):
        max_val = float("-inf")
        def dfs(node):
            if not node:
                return True
            nonlocal max_val
            if not dfs(node.left):
                return False
            if max_val >= node.val:
                return False
            max_val = node.val
            if not dfs(node.right):
                return False
            return True
        return dfs(root)
