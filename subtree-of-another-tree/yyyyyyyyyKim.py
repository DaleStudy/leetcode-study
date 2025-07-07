"""
LeetCode 572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/

summary:
root 트리 안에 subRoot 트리와 동일한 구조 & 값을 가진 서브트리가 있는지 확인
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # DFS
        # 시간복잡도 O(n*m) : n = root트리 노드 개수, m = subRoot트리 노드 개수
        # 공간복잡도 O(h1+h2) : h1 = root의 최대높이(최악O(n)), h2 = subRoot의 최대높이(최악O(m))
        # 두 트리의 구조와 값이 같은지 확인
        def isSameTree(node1, node2):
            # 둘 다 없으면 True
            if not node1 and not node2:
                return True
            # 둘 중 하나만 없으면 False
            if not node1 or not node2:
                return False
            # 현재 노드 값이 다르면 False
            if node1.val != node2.val:
                return False

            # root 트리랑 subRoot 트리의 양쪽 서브트리 재귀 탐색
            return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)

        # root 트리를 DFS로 돌면서 subRoot와 같은지 확인
        def dfs(node):
            if not node:
                return False
            if isSameTree(node, subRoot):
                return True

            # root 트리의 양쪽 서브트리 탐색    
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
