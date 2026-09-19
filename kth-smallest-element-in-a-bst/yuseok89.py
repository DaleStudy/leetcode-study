# TC: O(N)
# SC: O(H)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        ans = 0

        def rec(node: TreeNode | None) -> None:
            nonlocal k, ans

            if node is None or k <= 0:
                return

            rec(node.left)

            k -= 1
            if k == 0:
                ans = node.val
                return

            rec(node.right)

        rec(root)

        return ans

