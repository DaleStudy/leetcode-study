"""
Blind 75 - Maximum Depth of Binary Tree
LeetCode Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
시간복잡도 : O(n)
공간복잡도 : O(n)
풀이 : 재귀를 이용한 깊이 우선 탐색(DFS)
자식 노드부터 부모 노드로 거슬러 올라가며 최대 깊이를 계산합니다.
종료 조건 - left와 right가 모두 None인 경우 (1+max(0,0))을 반환하며 재귀가 종료됩니다.
"""

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
