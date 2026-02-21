# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val:idx for idx, val in enumerate(inorder) }
        preorder_iter = iter(preorder)

        def dfs(start, end):
            if start > end:
                return None

            val = next(preorder_iter)
            mid = inorder_idx[val]

            return TreeNode(val, dfs(start, mid-1), dfs(mid+1, end))
        
        return dfs(0, len(preorder)-1)
    
