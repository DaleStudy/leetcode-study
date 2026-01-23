# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = -1e9

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.getSum(root, 0)
        return self.answer

    def getSum(self, node, depth):
        val = node.val
        leftMax = self.getSum(node.left, depth+1) if node.left else 0
        rightMax = self.getSum(node.right, depth+1) if node.right else 0

        temp = val + (leftMax if leftMax > 0 else 0) + (rightMax if rightMax > 0 else 0)

        if self.answer < temp:
            self.answer = temp

        if leftMax > rightMax:
            val += leftMax if leftMax > 0 else 0
        else:
            val += rightMax if rightMax > 0 else 0
        
        return val