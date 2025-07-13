# https://leetcode.com/problems/subtree-of-another-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        [Complexity]
            - TC: O(n * m) (n = root 내 노드 개수, m = subRoot 내 노드 개수)
            - SC: O(n + m) (call stack)

        [Approach]
            다음과 같이 동작을 나눌 수 있다.
                (1) tree를 타고 내려가는 로직       : dfs
                (2) 두 tree가 동일한지 판단하는 로직  : check
        """

        def check(node1, node2):
            # base condition
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False

            # recur
            return (
                node1.val == node2.val  # 두 노드의 값이 같고
                and check(node1.left, node2.left)  # 하위 children도 모두 같아야 함
                and check(node1.right, node2.right)
            )

        def dfs(node, sub_tree):
            # base condition
            if not node:
                return False

            # recur
            return (
                check(node, sub_tree)  # 현재 node부터 sub_tree와 동일한지 확인
                or dfs(node.left, sub_tree)  # 동일하지 않다면, node.left로 타고 내려가서 확인
                or dfs(node.right, sub_tree)  # 동일하지 않다면, node.right로도 타고 내려가서 확인
            )

        return dfs(root, subRoot)
