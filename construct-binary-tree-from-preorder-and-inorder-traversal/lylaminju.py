from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {value: idx for idx, value in enumerate(inorder)}
        self.preorder_idx = 0

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            root_val = preorder[self.preorder_idx]
            self.preorder_idx += 1

            root = TreeNode(root_val)
            root.left = helper(left, inorder_map[root_val] - 1)
            root.right = helper(inorder_map[root_val] + 1, right)

            return root
        
        return helper(0, len(inorder) - 1)


# Time Complexity: O(n)
# - Each node is visited exactly once in preorder, and the dictionary lookup in inorder_map takes O(1) per node.

# Space Complexity: O(n)
# - The hash map (inorder_map) uses O(n) space.
# - The recursion stack uses up to O(h) space, where h is the height of the tree (O(n) in the worst case, O(log n) for a balanced tree).
