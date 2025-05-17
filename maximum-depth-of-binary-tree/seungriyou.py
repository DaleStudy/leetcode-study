# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth_recur(self, root: Optional[TreeNode]) -> int:
        """
        [Complexity]
            - TC: O(n) (모든 node를 한 번씩 방문)
            - SC: O(h) (call stack) (h = logn ~ n)

        [Approach] recursive
            재귀적으로 max(left subtree의 depth, right subtree의 depth) + 1 을 구하면 된다.
            base condition(= 현재 노드가 None인 경우)에서는 0을 반환한다.
        """

        def get_max_depth(node):
            # base condition
            if not node:
                return 0

            # recur
            return max(get_max_depth(node.right), get_max_depth(node.left)) + 1

        return get_max_depth(root)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        [Complexity]
            - TC: O(n) (모든 node를 한 번씩 방문)
            - SC: O(w) (트리의 너비) (w = 1 ~ n / 2)

        [Approach] iterative
            BFS 처럼 이진 트리를 레벨 별로 순회하며 depth를 1씩 증가시킬 수 있다.
        """
        depth = 0
        curr_level = [root] if root else []

        while curr_level:
            next_level = []
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            curr_level = next_level
            depth += 1

        return depth
