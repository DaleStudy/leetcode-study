# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        TC: O(n)
        SC: 최악의 경우 -> O(n), 평균 -> O(log n)
            - 트리가 균일할 경우 평균의 복잡도가 나오고
            - 한쪽이 치우친 경우 최악의 경우로 나온다.
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return validate(node.left, left, node.val) and validate(node.right, node.val, right)
        return validate(root, float("-inf"), float("inf"))
