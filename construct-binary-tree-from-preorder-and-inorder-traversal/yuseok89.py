# TC: O(N)
# SC: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0

        def build(left: int, right: int) -> TreeNode | None:
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

