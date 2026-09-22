# N is the number of nodes, and H is the height of the binary tree.
# TC: O(N) - visits each node once in post-order DFS
# SC: O(H) - recursion call stack proportional to tree height (O(N) in worst case)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def maxPathSum(self, root) -> int:
        max_sum = float("-inf")

        def max_gain(node) -> int:
            nonlocal max_sum
            if not node:
                return 0

            left_gain = max(0, max_gain(node.left))
            right_gain = max(0, max_gain(node.right))

            current_path = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path)

            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return max_sum
