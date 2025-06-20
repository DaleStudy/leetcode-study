# https://leetcode.com/problems/same-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(height) (call stack)

        [Approach]
            재귀적으로 두 tree를 타고 내려가며 확인할 수 있다.
            각 단계에서 두 tree가 다르다고 판단할 수 있는 조건은
                (1) 한 쪽 node만 None이거나
                (2) 두 node의 값이 다른
            경우이다.
        """
        # base condition
        if not p and not q:
            return True

        # not same
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
