from typing import Optional
from unittest import TestCase, main


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.solve_dfs(root)

    """
    Runtime: 11 ms (Beats 98.62%)
    Time Complexity: O(n)
    > dfs를 통해 모든 node를 방문하므로 O(n)

    Memory: 22.10 MB (Beats 10.70%)
    Space Complexity: O(n)
        - dfs 재귀 호출 스택의 깊이는 이진트리가 최악으로 편향된 경우 O(n), upper bound
        - 나머지 변수는 O(1)
        > O(n), upper bound
    """
    def solve_dfs(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_path_sum

            if not node:
                return 0

            max_left = max(dfs(node.left), 0)
            max_right = max(dfs(node.right), 0)
            max_path_sum = max(max_path_sum, node.val + max_left + max_right)

            return node.val + max(max_left, max_right)

        dfs(root)

        return max_path_sum


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        root = TreeNode(-10)
        node_1 = TreeNode(9)
        node_2 = TreeNode(20)
        node_3 = TreeNode(15)
        node_4 = TreeNode(7)
        node_2.left = node_3
        node_2.right = node_4
        root.left = node_1
        root.right = node_2

        # root = [-10, 9, 20, None, None, 15, 7]
        output = 42

        self.assertEqual(Solution().maxPathSum(root), output)


if __name__ == '__main__':
    main()
