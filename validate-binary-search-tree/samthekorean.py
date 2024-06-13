# TC : O(n) where n being the number of nodes of the tree
# SC : O(n) where n being the size of sum of every nodes
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst(node, min_val, max_val):
            if not node:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            return is_valid_bst(node.left, min_val, node.val) and is_valid_bst(
                node.right, node.val, max_val
            )

        return is_valid_bst(root, float("-inf"), float("inf"))
