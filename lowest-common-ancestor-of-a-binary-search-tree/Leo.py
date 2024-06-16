class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while True:
            if root.val < min(p.val, q.val):
                root = root.right

            elif root.val > max(p.val, q.val):
                root = root.left

            else:
                return root

        # TC: O(n) where n is height of the tree, SC: O(1)
