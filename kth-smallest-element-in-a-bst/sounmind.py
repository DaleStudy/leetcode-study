# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        def inorderTraverse(node: Optional[TreeNode]):
            if node is None or len(result) >= k:
                return

            inorderTraverse(node.left)

            if len(result) < k:
                result.append(node.val)

            inorderTraverse(node.right)

        inorderTraverse(root)

        return result[k - 1]


# Time Complexity: O(N)
# In the worst case, we need to visit all the nodes in the tree.
# Thus, the time complexity is O(N), where N is the number of nodes in the tree.

# Space Complexity: O(N)
# The space complexity is determined by the recursion stack and the result list.
# 1. Recursion stack: In the worst case (unbalanced tree), the recursion stack can go up to N levels deep, so the space complexity is O(N).
#    In the best case (balanced tree), the recursion stack depth is log(N), so the space complexity is O(log N).
# 2. Result list: The result list stores up to k elements, so the space complexity is O(k).
