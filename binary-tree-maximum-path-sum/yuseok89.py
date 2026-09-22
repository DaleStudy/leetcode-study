# TC: O(N)
# SC: O(H)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        ans = float('-inf')

        def get_max(cur: Optional[TreeNode]) -> int:
            nonlocal ans

            if cur is None:
                return 0

            left_max = get_max(cur.left)
            right_max = get_max(cur.right)

            ans = max(ans, cur.val, cur.val + left_max, cur.val + right_max, cur.val +left_max + right_max)

            return max(cur.val, cur.val + max(left_max, right_max))

        get_max(root)

        return ans

