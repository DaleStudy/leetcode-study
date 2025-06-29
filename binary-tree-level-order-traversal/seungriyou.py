# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder_bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(width) (최악의 경우 O(n)) (결과 res 제외)

        [Approach]
            레벨 별로 BFS로 접근
        """
        if not root:
            return []

        res, level = [], [root]

        while level:
            # res에 현재 level 내 node value 추가
            res.append([node.val for node in level])

            # next level의 node로 level 업데이트
            level = [child for node in level for child in (node.left, node.right) if child]
            # next_level = []
            # for node in level:
            #     if node.left:
            #         next_level.append(node.left)
            #     if node.right:
            #         next_level.append(node.right)
            # level = next_level

        return res

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(height) (call stack) (결과 res 제외)

        [Approach]
            레벨 별로 DFS로 접근
        """
        if not root:
            return []

        res = []

        def dfs(node, level):
            # base condition (각 level의 첫 시작)
            if len(res) == level:
                res.append([])

            # 현재 level에 node.val 추가
            res[level].append(node.val)

            # node의 child에 대해 다음 level로 진행
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        dfs(root, 0)

        return res
