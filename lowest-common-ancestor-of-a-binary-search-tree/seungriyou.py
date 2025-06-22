# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor_recur(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        [Complexity]
            - TC: O(height)
            - SC: O(height) (call stack)

        [Approach]
            어떤 node와 두 노드 p, q 간의 관계를 다음의 케이스로 나누어 볼 수 있다.
                1) p와 q가 모두 현재 node 보다 작다면 --> left subtree로 내려가 살펴보기
                2) p와 q가 모두 현재 node 보다 크다면 --> right subtree로 내려가 살펴보기
                3) p와 q가 현재 node의 두 child subtree에 각각 존재한다면 --> 현재 node가 p, q의 LCA
        """

        def find_lca(node):
            # 1) p와 q가 모두 현재 node 보다 작다면 --> left subtree로 내려가 살펴보기
            if p.val < node.val > q.val:
                return find_lca(node.left)
            # 2) p와 q가 모두 현재 node 보다 크다면 --> right subtree로 내려가 살펴보기
            if p.val > node.val < q.val:
                return find_lca(node.right)
            # 3) p와 q가 현재 node의 두 child subtree에 각각 존재한다면 --> 현재 node가 p, q의 LCA
            return node

        return find_lca(root)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        [Complexity]
            - TC: O(height)
            - SC: O(1)

        [Approach]
            이전 recursive 풀이를 iterative 하게 풀이할 수 있다.
        """
        while root:
            # 1) p와 q가 모두 현재 node 보다 작다면 --> left subtree로 내려가 살펴보기
            if p.val < root.val > q.val:
                root = root.left
            # 2) p와 q가 모두 현재 node 보다 크다면 --> right subtree로 내려가 살펴보기
            elif p.val > root.val < q.val:
                root = root.right
            # 3) p와 q가 현재 node의 두 child subtree에 각각 존재한다면 --> 현재 node가 p, q의 LCA
            else:
                return root
