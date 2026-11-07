# N is the number of nodes in the binary tree.
# TC: O(N) - building hashmap takes O(N), and each node is visited once in O(1) time
# SC: O(N) - hashmap takes O(N) space, and recursion call stack takes O(H) up to O(N)

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_idx

            if left > right:
                return None

            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)
            preorder_idx += 1

            mid = inorder_map[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
