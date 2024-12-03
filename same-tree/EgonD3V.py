from typing import Optional
from unittest import TestCase, main


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.solve_dfs(p, q)

    """
    Runtime: 0 ms (Beats 100.00%)
    Time Complexity: O(min(p, q))
    > dfs를 통해 모든 node를 방문하므로, 각 트리의 node의 갯수를 각각 p, q라 하면, O(min(p, q))

    Memory: 16.62 MB (Beats 15.78%)
    Space Complexity: O(min(p, q))
    > 일반적인 경우 트리의 깊이만큼 dfs 호출 스택이 쌓이나, 최악의 경우 한쪽으로 편향되었다면 O(min(p, q)), upper bound
    """
    def solve_dfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            elif (p is not None and q is not None) and (p.val == q.val):
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            else:
                return False

        return dfs(p, q)


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        p_1 = TreeNode(1)
        p_2 = TreeNode(2)
        p_3 = TreeNode(3)
        p_1.left = p_2
        p_1.right = p_3

        q_1 = TreeNode(1)
        q_2 = TreeNode(3)
        q_3 = TreeNode(3)
        q_1.left = q_2
        q_1.right = q_3

        self.assertEqual(Solution().isSameTree(p_1, q_1), True)


if __name__ == '__main__':
    main()
