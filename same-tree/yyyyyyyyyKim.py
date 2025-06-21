# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # DFS
        # 시간복잡도 O(n), 공간복잡도 O(n)
        def dfs(node1, node2):
            # 둘 다 없으면 같은 트리
            if not node1 and not node2:
                return True
            # 둘 중 하나만 없으면 다른 트리
            if not node1 or not node2:
                return False
            # 둘의 값이 다르면 다른 트리
            if node1.val != node2.val:
                return False
            # 좌우서브트리 비교
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

        return dfs(p, q)
