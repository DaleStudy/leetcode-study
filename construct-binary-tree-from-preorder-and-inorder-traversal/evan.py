from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder.pop(0)

        root_inorder_index = inorder.index(root_val)

        left_tree_inorder = inorder[:root_inorder_index]
        right_tree_inorder = inorder[root_inorder_index + 1 :]

        return TreeNode(
            root_val,
            self.buildTree(preorder, left_tree_inorder),
            self.buildTree(preorder, right_tree_inorder),
        )


# Overall time complexity: O(N^2)
# - Finding the root in the inorder list and splitting it takes O(N) time in each call.
# - There are N nodes, so this operation is repeated N times.

# Overall space complexity: O(N)
# - The primary space usage is the recursion stack which goes as deep as the height of the tree.
# - In the worst case (unbalanced tree), this can be O(N).
# - In the best case (balanced tree), this is O(log N).
