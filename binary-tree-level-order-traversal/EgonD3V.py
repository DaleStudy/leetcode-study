from collections import deque
from typing import Optional, List
from unittest import TestCase, main


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.solve_dfs(root)

    """
    Runtime: 0 ms (Beats 100.00%)
    Time Complexity: O(n)
        > 각 node를 bfs 방식으로 한 번 씩 조회하므로 O(n)

    Memory: 17.42 (Beats 11.96%)
    Space Complexity: O(n)
        > 최악의 경우, deque에 최대 node의 갯수만큼 저장될 수 있으므로 O(n), upper bound
    """
    def solve_bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dq = deque([root])
        result = []
        while dq:
            tmp_result = []
            for _ in range(len(dq)):
                curr = dq.popleft()
                tmp_result.append(curr.val)

                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)

            result.append(tmp_result)

        return result

    """
    Runtime: 1 ms (Beats 38.71%)
    Time Complexity: O(n)
        > 각 node를 dfs 방식으로 한 번 씩 조회하므로 O(n)

    Memory: 17.49 (Beats 11.96%)
    Space Complexity: O(1)
        > 최악의 경우, list에 최대 node의 갯수만큼 저장될 수 있으므로 O(n), upper bound
    """
    def solve_dfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        def dfs(node: TreeNode, depth: int):
            if len(result) <= depth:
                result.append([node.val])
            else:
                result[depth].append(node.val)

            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        result = []
        dfs(root, 0)

        return result


class _LeetCodeTestCases(TestCase):

    def test_1(self):
        root = TreeNode(3)
        node1 = TreeNode(9)
        node2 = TreeNode(20)
        node3 = TreeNode(15)
        node4 = TreeNode(7)
        root.left = node1
        root.right = node2
        node2.left = node3
        node2.right = node4
        output = [[3], [9, 20], [15, 7]]
        self.assertEqual(Solution.levelOrder(Solution(), root), output)

    def test_2(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)
        root.left = node1
        root.right = node2
        node1.left = node3
        node2.left = node4
        output = [[1], [2, 3], [4, 5]]
        self.assertEqual(Solution.levelOrder(Solution(), root), output)


if __name__ == '__main__':
    main()
