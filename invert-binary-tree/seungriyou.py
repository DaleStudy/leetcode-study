# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree_recur1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        [Complexity]
            - TC: O(n) (모든 노드 방문)
            - SC: O(height) (call stack)

        [Approach]
            DFS 처럼 recursive 하게 접근한다.
        """

        def invert(node):
            # base condition
            if not node:
                return

            # recur (& invert the children)
            node.left, node.right = invert(node.right), invert(node.left)

            return node

        return invert(root)

    def invertTree_recur(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(height) (call stack)

        [Approach]
            recursive 한 방법에서 base condition 처리 로직을 더 짧은 코드로 나타낼 수 있다.
        """

        def invert(node):
            if node:
                # recur (& invert the children)
                node.left, node.right = invert(node.right), invert(node.left)
            return node

        return invert(root)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(width) (queue)

        [Approach]
            BFS 처럼 iterative 하게 접근한다.
        """
        from collections import deque

        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                # invert the children
                node.left, node.right = node.right, node.left

                # add to queue
                q.append(node.left)
                q.append(node.right)

        return root
