from typing import List, Optional
from unittest import TestCase, main


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.solve_1(preorder, inorder)

    """
    Runtime: 112 ms (Beats 66.16%)
    Time Complexity: O(n ** 2)
    Space Complexity: O(n)
    Memory: 52.83 MB (Beats 63.14%)
    """
    def solve_1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = 0

        def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            nonlocal index

            if not inorder:
                return None

            if not 0 <= index < len(preorder):
                return None

            root = TreeNode(preorder[index])
            index += 1
            split_index = inorder.index(root.val)
            root.left = build_tree(preorder, inorder[:split_index])
            root.right = build_tree(preorder, inorder[split_index + 1:])

            return root

        return build_tree(preorder, inorder)


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        output = TreeNode(
            val=3,
            left=TreeNode(
                val=9
            ),
            right=TreeNode(
                val=20,
                left=TreeNode(val=15),
                right=TreeNode(val=7)
            )
        )
        self.assertEqual(Solution.buildTree(Solution(), preorder, inorder), output)

    def test_2(self):
        preorder = [-1]
        inorder = [-1]
        output = TreeNode(
            val=-1
        )
        self.assertEqual(Solution.buildTree(Solution(), preorder, inorder), output)

    def test_3(self):
        preorder = [1, 2]
        inorder = [1, 2]
        output = TreeNode(
            val=1,
            right=TreeNode(
                val=2
            )
        )
        self.assertEqual(Solution.buildTree(Solution(), preorder, inorder), output)


if __name__ == '__main__':
    main()
