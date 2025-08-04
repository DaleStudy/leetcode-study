# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional
import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST1(self, root: Optional['TreeNode']) -> bool:
        """
        [Complexity]
            - TC: O(n) (모든 node 한 번씩 방문)
            - SC: O(h) (recursion call stack) (balanced tree라면 O(logn), skewed tree라면 O(n))

        [Approach]
            valid한 BST는 다음을 만족해야 하므로 recursion을 이용해서 풀 수 있다.
                1) left subtree는 less than key
                2) right subtree는 greater than key
                3) left & right subtree도 BST
            이때, 각 subtree를 recursive 하게 타고 들어가서 확인하려면, 각 단계에서 node, min floor val, max ceil val이 필요하고
            각 단계(= is_valid_subtree())는 다음과 같이 분기를 나눠 진행할 수 있다.
                1) node가 None일 때 (base condition): True 반환
                2) 현재 노드의 값인 node.val이 min floor ~ max ceil 범위에 해당하지 않을 때: False 반환
                3) 그 외: left subtree와 right subtree도 valid 한지 재귀적으로 확인
        """

        def is_valid_subtree(node, floor, ceil):
            if not node:
                return True

            if not (floor < node.val < ceil):
                return False

            return is_valid_subtree(node.left, floor, node.val) and is_valid_subtree(node.right, node.val, ceil)

        return is_valid_subtree(root, -math.inf, math.inf)

    def isValidBST(self, root: Optional['TreeNode']) -> bool:
        """
        [Complexity]
            - TC: O(n) (모든 node 한 번씩 방문)
            - SC: O(n) (recursion call stack O(h) + path O(n))

        [Approach]
            inorder traversal 후, 원소가 모두 항상 strictly ascending sorted 되어 있는지 확인하면 된다.
        """

        path = []
        is_asc = True

        def inorder(node):
            nonlocal is_asc

            if not node:
                return

            inorder(node.left)

            # path에 원소가 asc 정렬되지 않은 채로 들어간다면, is_asc = False로 변경
            if path and path[-1] >= node.val:
                is_asc = False
            path.append(node.val)

            inorder(node.right)

        inorder(root)

        return is_asc
