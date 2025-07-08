# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
트리를 유일하게 복원하기 위해서는 inorder가 필요하다. inorder는 left/right child를 구분할 수 있기 때문이다.
    - preorder + inorder: root를 먼저 알고, inorder로 구조 구분
    - postorder + postorder: root를 나중에 알고, inorder로 구조 구분
preorder + postorder라면, 구조가 다른 트리를 구분할 수 없는 경우가 있다.
"""

class Solution:
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        [Complexity]
            - TC: O(n^2)
            - SC: O(n^2)
            (* pop(0), index(), slicing이 모두 O(n))

        [Approach]
            preorder의 경우, root - left - right 순서로 방문하므로, root를 제일 먼저 찾을 수 있다.
            inorder의 경우, left - root - right 순서로 방문하므로,
            preorder의 매 단계에서 찾은 root에 대해 left와 right subtree를 다음과 같이 정의할 수 있다. (root 제외)
                - left subtree = inorder[:root_idx]
                - right subtree = inorder[root_idx + 1:]
        """
        root = None

        if inorder:
            # preorder root
            root_idx = inorder.index(preorder.pop(0))
            root = TreeNode(val=inorder[root_idx])
            # preorder left
            root.left = self.buildTree(preorder, inorder[:root_idx])
            # preorder right
            root.right = self.buildTree(preorder, inorder[root_idx + 1:])

        return root

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        [Complexity]
            - TC: O(n^2)
            - SC: O(n^2)
            (* index(), slicing이 모두 O(n))

        [Approach]
            이전 코드에서 pop(0)에 드는 O(n)을 줄이기 위해,
            preorder.reverse() 후 pop()으로 변경할 수 있다.
        """
        preorder.reverse()

        def solve(preorder, inorder):
            if inorder:
                # preorder root
                root_idx = inorder.index(preorder.pop())
                root = TreeNode(inorder[root_idx])
                # preorder left
                root.left = solve(preorder, inorder[:root_idx])
                # preorder right
                root.right = solve(preorder, inorder[root_idx + 1:])

                return root

        return solve(preorder, inorder)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n) (call stack)

        [Approach]
            병목이었던 index()와 slicing을 O(1)로 최적화 할 수 있다.
                - index(): inorder의 index를 dict로 캐싱
                - slicing: start/end index로 추적
            이와 더불어 preorder의 root를 가리키는 index인 pre_idx를 사용하면 pop(0) 또는 pop()을 대체할 수도 있다.
        """

        # instead of index()
        inorder_idx = {num: i for i, num in enumerate(inorder)}

        # preorder root (instead of pop())
        pre_idx = 0

        # instead of inorder[in_left:in_right] slicing
        def solve(in_left, in_right):
            nonlocal pre_idx

            # base condition
            if in_left >= in_right:
                return

            # preorder root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # update indices
            root_idx = inorder_idx[root_val]
            pre_idx += 1

            # recur
            root.left = solve(in_left, root_idx)
            root.right = solve(root_idx + 1, in_right)

            return root

        return solve(0, len(inorder))
