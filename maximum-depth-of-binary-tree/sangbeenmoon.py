# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC : O(n)
# SC : O(n)

class Solution:
    answer = 0

    def go(self, cur: TreeNode, depth:int):
        self.answer = max(self.answer, depth)
        if cur.left != None:
            self.go(cur.left, depth + 1)
        if cur.right != None:
            self.go(cur.right, depth + 1)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        
        if root != None:
            self.go(root, 1)

        return self.answer
