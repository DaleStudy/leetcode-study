from typing import Optional
from unittest import TestCase, main


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.solve_dfs_iterable(root)

    """
    Runtime: 0 ms (Beats 100.00%)
    Time Complexity: O(n)
    > 트리의 모든 노드의 갯수를 n개라고 하면, 트리의 모든 노드를 stack에 넣어 조회하므로 O(n)

    Memory: 17.75 MB (Beats 21.97%)
    Space Complexity: O(n)
    > 최악의 경우 트리의 최대 길이가 n인 경우이므로, stack의 최대 크기가 n에 비례하므로 O(n), upper bound
    """
    def solve_dfs_iterable(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        stack = [(root, 0)]
        while stack:
            curr_node, curr_depth = stack.pop()
            if curr_node is None:
                continue

            if curr_node.left is None and curr_node.right is None:
                max_depth = max(max_depth, curr_depth + 1)
                continue

            if curr_node.left:
                stack.append((curr_node.left, curr_depth + 1))
            if curr_node.right:
                stack.append((curr_node.right, curr_depth + 1))

        return max_depth


    """
    Runtime: 0 ms (Beats 100.00%)
    Time Complexity: O(n)
    
    Memory: 17.90 MB (Beats 9.05%)
    Space Complexity: O(n)
    """
    def solve_dfs_recursive(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def dfs(node: Optional[TreeNode], depth: int):
            nonlocal max_depth

            if not node:
                return max_depth

            if node.left is None and node.right is None:
                max_depth = max(max_depth, depth + 1)
                return

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return max_depth


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    main()
