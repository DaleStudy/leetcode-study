# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
            
        val = preorder.pop(0)
        mid = inorder.index(val)
        left = self.buildTree(preorder, inorder[:mid])
        right = self.buildTree(preorder, inorder[mid + 1 :])
        return TreeNode(val, left, right)
