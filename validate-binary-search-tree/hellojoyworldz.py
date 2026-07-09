# 문제: https://leetcode.com/problems/validate-binary-search-tree/
# 해설: https://www.algodale.com/problems/validate-binary-search-tree/
# 위치: https://github.com/DaleStudy/leetcode-study/tree/main/validate-binary-search-tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return check(node.left, low, node.val) and check(node.right, node.val, high)

        return check(root, float("-inf"), float("inf"))

