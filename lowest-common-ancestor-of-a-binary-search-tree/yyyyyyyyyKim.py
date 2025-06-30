# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # BST(이진 탐색 트리) 특성 활용해서 밸류값으로 LCA 찾기
        # 시간복잡도 O(log n)/ 최악O(n), 공간복잡도 O(1)
        while root:
            # p, q가 둘 다 root보다 작으면, LCA는 왼쪽 서브트리에 있음
            if p.val < root.val and q.val < root.val:
                root = root.left
            # p, q가 둘 다 root보다 크면, LCA는 오른쪽 서브트리에 있음
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # p, q가 root의 양쪽에 나눠져 있는 경우 -> root가 LCA
            else:
                return root
