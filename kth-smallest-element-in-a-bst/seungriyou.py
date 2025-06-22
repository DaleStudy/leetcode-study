# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest_recur(self, root: Optional[TreeNode], k: int) -> int:
        """
        [Complexity]
            - TC: O(k)
            - SC: O(height) (call stack)

        [Approach]
            BST를 inorder로 순회하면 오름차순으로 node를 방문할 수 있다. (recursive)
            각 호출에서 cnt를 세며 k와 같을 때 res 값을 기록한다.
        """
        cnt, res = 0, None

        def inorder(node):
            nonlocal cnt, res

            # base condition
            if not node or res:
                return

            # recur
            inorder(node.left)
            cnt += 1
            if cnt == k:
                res = node.val
            inorder(node.right)

        inorder(root)

        return res

    def kthSmallest_recur2(self, root: Optional[TreeNode], k: int) -> int:
        """
        [Complexity]
            - TC: O(k)
            - SC: O(height) (call stack)

        [Approach]
            이전 recursive 풀이를 generator 방식으로 바꿀 수 있다. (yield from으로 recursion 구현)
        """

        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node
                yield from inorder(node.right)

        for i, node in enumerate(inorder(root), start=1):
            if i == k:
                return node.val

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        [Complexity]
            - TC: O(k)
            - SC: O(height) (stack에는 최대 height 개의 node가 들어감)

        [Approach]
            BST의 inorder 순회를 stack을 이용하여 iterative 하게 풀이할 수 있다.
        """
        cnt, stack = 0, []

        # root에서부터 left child를 stack에 넣기
        while root:
            stack.append(root)
            root = root.left

        # leaf left child 부터 stack에서 pop
        while stack:
            node = stack.pop()
            cnt += 1

            if cnt == k:
                return node.val

            # 현재 node의 right child가 있다면 stack에 넣고
            right = node.right
            while right:
                # right child에서부터 left child를 stack에 넣기
                stack.append(right)
                right = right.left
