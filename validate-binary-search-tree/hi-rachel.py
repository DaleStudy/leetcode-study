# O(n) time, O(n) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 좌측 서브 트리로 내려갈 떄:
#     - 하한값: 부모 노드의 하한값
#     - 상한값: 부모 노드의 값
# 우측 서브 트리로 내려갈 때:
#     - 하한값: 부모 노드의 값
#     - 상한값: 부모 노드의 상한값

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float('-inf'), float("inf"))
    