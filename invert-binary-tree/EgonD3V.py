from typing import Optional
from unittest import TestCase, main


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.solve_dfs(root)

    """
    Runtime: 0 ms (Beats 100.00%)
    Time Complexity: O(n)
    > 트리의 모든 node를 방문하므로 O(n)

    Memory: 16.53 MB (Beats 25.95%)
    Space Complexity: O(n)
    > stack의 최대 크기는 트리의 최장 경로를 이루는 node의 갯수이고, 최악의 경우 트리의 한 쪽으로 모든 node가 이어져있는 경우이므로 O(n), upper bound
    """
    def solve_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        stack = [root]
        while stack:
            curr_node = stack.pop()
            curr_node.left, curr_node.right = curr_node.right, curr_node.left
            if curr_node.left:
                stack.append(curr_node.left)
            if curr_node.right:
                stack.append(curr_node.right)

        return root


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        return


if __name__ == '__main__':
    main()
