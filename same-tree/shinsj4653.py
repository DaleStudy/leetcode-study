"""
[문제풀이]
# Inputs
두 이진 트리의 노드 배열들 p, q

# Outputs
두 트리가 같은지 다른지 체크

# Constraints
- The number of nodes in both trees is in the range [0, 100].
- -104 <= Node.val <= 104

# Ideas
둘 다 bfs?? 때리면 될 것 같은데?
동시에 탐색하면서 다른 노드 나오면 바로 종료

[회고]
풀긴 풀었는데 좀 더 깔금한 풀이가 있을까?
->

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p_tree, q_tree):
            print('p: ', p_tree)
            print('q: ', q_tree)

            if p_tree is not None and q_tree is not None and p_tree.val == q_tree.val:
                print('add left and right')
                return dfs(p_tree.left, q_tree.left) and dfs(p_tree.right, q_tree.right)

            if (p_tree == q_tree == None):
                return True

            if (p_tree is not None and q_tree is None) or \
                    (p_tree is None and q_tree is not None) or \
                    (p_tree is not None and q_tree is not None and p_tree.val != q_tree.val):
                print("not same!!")
                return False

        return dfs(p, q)

# 해설
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)





