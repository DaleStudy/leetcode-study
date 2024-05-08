"""
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/description/

Solution
    Recursively swaps the left and right children of the root node.

    1. Check if the root has left and right children.
    2. If it does, invert the left and right children.
    3. If it doesn't, invert the left or right child.
    4. Return the root.

Time complexity: O(n)
Space complexity: O(n)

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        has_left = hasattr(root, "left")
        has_right = hasattr(root, "right")

        if has_left and has_right:
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)
            root.left, root.right = root.right, root.left
        elif has_left:
            root.left = self.invertTree(root.left)
            root.left, root.right = None, root.left
        elif has_right:
            root.right = self.invertTree(root.right)
            root.left, root.right = root.right, None

        return root


def main():
    test_cases = [
        [
            TreeNode(
                4,
                TreeNode(2, TreeNode(1), TreeNode(3)),
                TreeNode(7, TreeNode(6), TreeNode(9)),
            ),
            TreeNode(
                4,
                TreeNode(7, TreeNode(9), TreeNode(6)),
                TreeNode(2, TreeNode(3), TreeNode(1)),
            ),
        ],
        [
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(2, TreeNode(3), TreeNode(1)),
        ],
        [
            TreeNode(),
            TreeNode(),
        ],
    ]
    s = Solution()

    for test_case in test_cases:
        root_input, expected = test_case
        assert s.invertTree(root_input) == expected


if __name__ == "__main__":
    main()
