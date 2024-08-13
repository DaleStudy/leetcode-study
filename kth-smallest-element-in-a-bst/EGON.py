from typing import Optional, List
from unittest import TestCase, main
from heapq import heappush, heappop


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.solve_2(root, k)

    """
    Runtime: 50 ms (Beats 25.03%)
    Analyze Complexity: O(n)
    Memory: 19.55 MB (Beats 15.91%)
    """
    def solve_1(self, root: Optional[TreeNode], k: int) -> int:
        visited = []
        stack = [root]
        while stack:
            curr_node = stack.pop()
            heappush(visited, curr_node.val)
            if curr_node.left is not None:
                stack.append(curr_node.left)
            if curr_node.right is not None:
                stack.append(curr_node.right)

        result = visited[0]
        for _ in range(k):
            result = heappop(visited)

        return result

    """
    Runtime: 43 ms (Beats 69.91%)
    Analyze Complexity: O(n)
    Memory: 19.46 MB (Beats 60.94%)
    """
    def solve_2(self, root: Optional[TreeNode], k: int) -> int:
        vals = []

        def inorder_traverse(root: Optional[TreeNode]):
            if root is None:
                return

            if len(vals) >= k:
                return

            inorder_traverse(root.left)
            vals.append(root.val)
            inorder_traverse(root.right)

        inorder_traverse(root)
        return vals[k - 1]


class _LeetCodeTCs(TestCase):
    def test_1(self):
        root = TreeNode(
            val=3,
            left=TreeNode(
                val=1,
                left=None,
                right=TreeNode(
                    val=2,
                    left=None,
                    right=None,
                )
            ),
            right=TreeNode(
                val=4,
                left=None,
                right=None
            )
        )

        k = 1
        output = 1
        self.assertEqual(Solution.kthSmallest(Solution(), root, k), output)

    def test_2(self):
        root = TreeNode(
            val=5,
            left=TreeNode(
                val=3,
                left=TreeNode(
                    val=2,
                    left=TreeNode(
                        val=1
                    )
                ),
                right=TreeNode(
                    val=4
                )
            ),
            right=TreeNode(
                val=6
            )
        )
        k = 3
        output = [3]
        self.assertEqual(Solution.kthSmallest(Solution(), root, k), output)


if __name__ == '__main__':
    main()
