"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
두 개의 정수 배열 preorder와 inoder가 주어졌을 때 이진 트리를 구성하고 반환하시오.
preorder = 전위 순회 : 루트 -> 왼쪽 서브트리 -> 오른쪽 서브트리
inorder = 중위 순회 : 왼쪽 서브트리 -> 루트 -> 오른쪽 서브트리

TC: O(n), n: 노드 수
SC: O(n)
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # 1. preorder의 첫 값이 root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # 2. inorder에서 root 위치 찾기
        root_index = inorder.index(root_val)

        # 3. 왼쪽, 오른쪽 나눠서 재귀적으로 연결
        root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])

        return root
