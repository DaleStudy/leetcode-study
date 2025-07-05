# 주어진 BST와 노드 p, q가 주어질 때
# 이 둘의 가장 가까운 공통 조상(Lowest Common Ancestor, LCA)을 찾아 반환해라
# 공통 조상이란, p와 q 모두의 조상 중에서 가장 깊은 노드를 의미
#
# BST(Binary Search Tree)의 특징
# - 각 노드는 최대 두 개의 자식 노드를 가질 수 있음
# - 왼쪽 서브트리의 모든 값은 현재 노드보다 작고,
# - 오른쪽 서브트리의 모든 값은 현재 노드보다 큼.
# 
# 풀이
# 현재 노드가 p, q보다 둘 다 작으면, 오른쪽 서브트리에서 LCA를 찾고,
# 둘 다 크면, 왼쪽 서브 트리에서 찾고,
# 한쪽은 작고, 한쪽은 크면 현재 노드가 LCA가 됨.

# TC: O(H), H는 이진 검색 트리의 높이
# SC: O(H), 재귀 스택에 필요한 공간

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 재귀 풀이
# TC: O(H), H는 이진 검색 트리의 높이
# SC: O(H), 재귀 스택에 필요한 공간
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

# 반복 풀이
# TC: O(H), H는 이진 검색 트리의 높이
# SC: O(1)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                return node
