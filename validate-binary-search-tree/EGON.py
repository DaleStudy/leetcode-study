from typing import Optional
from unittest import TestCase, main


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.solve_dfs(root)

    """
    Runtime: 0 ms (Beats 100.00%)
    Time Complexity: O(n)
        > root 트리의 노드의 갯수를 n이라 하면, 모든 node를 조회하므로 O(n)

    Memory: 18.91 MB (Beats 5.70%)
    Space Complexity: O(n)
        > root 트리의 높이만큼 is_valid_bst 함수가 재귀 호출 스택에 쌓이나, 문제의 제약조건에서 이진트리라고만 했으므로 편향될 수 있으므로, O(n), upper bound
    """
    def solve_dfs(self, root: Optional[TreeNode]) -> bool:

        def is_valid_bst(node: Optional[TreeNode], lower_bound=float('-inf'), upper_bound=float('inf')):
            if not node:
                return True

            if lower_bound < node.val < upper_bound:
                return is_valid_bst(node.left, lower_bound, node.val) and is_valid_bst(node.right, node.val, upper_bound)
            else:
                return False

        return is_valid_bst(root)


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)

        output = True

        self.assertEqual(Solution().isValidBST(root), output)

    def test_2(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(6)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(7)

        output = False

        self.assertEqual(Solution().isValidBST(root), output)


if __name__ == '__main__':
    main()
