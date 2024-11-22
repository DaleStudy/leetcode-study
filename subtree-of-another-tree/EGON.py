from typing import Optional
from unittest import TestCase, main


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.solve_dfs(root, subRoot)

    """
    Runtime: 35 ms (Beats 90.24%)
    Time Complexity: O(n)
        - root 트리의 크기를 n이라 하면, root 트리의 모든 노드를 조회하는데 O(n)
            - 각 노드마다 is_same_tree 실행하는데, subRoot 트리의 크기를 m이라 하면, 최대 subRoot의 노드의 크기만큼 조회하므로 * O(m)
        > O(n) * O(m) ~= O(n * m)

    Memory: 17.09 (Beats 9.93%)
    Space Complexity: O(max(n, m))
        - stack의 최대 크기는 root 트리가 편향된 경우이며, 이는 root 트리의 노드의 총 갯수와 같으므로 O(n), upper bound
        - is_same_tree 함수의 재귀 스택의 최대 깊이는 subRoot 트리가 편향된 경우이며, 이는 subRoot 트리의 노드의 총 갯수와 같으므로 O(m), upper bound
        > O(n) + O(m) ~= O(max(n, m))
    """
    def solve_dfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            elif (p is not None and q is not None) and (p.val == q.val):
                return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
            else:
                return False

        result = False
        stack = [root]
        while stack:
            curr = stack.pop()
            if (curr and subRoot) and curr.val == subRoot.val:
                result = result or is_same_tree(curr, subRoot)

            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)

        return result


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        root = TreeNode(3)
        root_1 = TreeNode(4)
        root_2 = TreeNode(5)
        root.left = root_1
        root.right = root_2
        root_3 = TreeNode(1)
        root_4 = TreeNode(2)
        root.left.left = root_3
        root.left.right = root_4

        subRoot = TreeNode(4)
        sub_1 = TreeNode(1)
        sub_2 = TreeNode(2)
        subRoot.left = sub_1
        subRoot.right = sub_2

        output = True
        self.assertEqual(Solution.isSubtree(Solution(), root, subRoot), output)

    def test_2(self):
        root = TreeNode(3)
        root_1 = TreeNode(4)
        root_2 = TreeNode(5)
        root.left = root_1
        root.right = root_2
        root_3 = TreeNode(1)
        root_4 = TreeNode(2)
        root.left.left = root_3
        root.left.right = root_4
        root_5 = TreeNode(0)
        root_4.left = root_5

        subRoot = TreeNode(4)
        sub_1 = TreeNode(1)
        sub_2 = TreeNode(2)
        subRoot.left = sub_1
        subRoot.right = sub_2

        output = False
        self.assertEqual(Solution.isSubtree(Solution(), root, subRoot), output)

    def test_3(self):
        root = TreeNode(1)
        root.right = TreeNode(1)
        root.right.right = TreeNode(1)
        root.right.right.right = TreeNode(1)
        root.right.right.right.right = TreeNode(1)
        root.right.right.right.right.right = TreeNode(2)

        subRoot = TreeNode(1)
        subRoot.right = TreeNode(1)
        subRoot.right.right = TreeNode(2)

        output = True
        self.assertEqual(Solution.isSubtree(Solution(), root, subRoot), output)


if __name__ == '__main__':
    main()
