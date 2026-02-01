# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.searchTree(p, q)

    def searchTree(self, node1, node2):
        if (not node1 and node2) or (node1 and not node2):
            return False
        elif not node1 and not node2:
            return True
        elif node1.val != node2.val:
            return False
        
        if node1.left and node2.left:
            left = self.searchTree(node1.left, node2.left)
        elif not node1.left and not node2.left:
            left = True
        else:
            return False

        if node1.right and node2.right:
            right = self.searchTree(node1.right, node2.right)
        elif not node1.right and not node2.right:
            right = True
        else:
            return False
        return left and right
    
