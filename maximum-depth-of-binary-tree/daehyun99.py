# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        stacks1 = [root]
        stacks2= []

        if root is None:
            return count
        while len(stacks1) > 0 :
            count += 1
            while len(stacks1) > 0 :
                node = stacks1.pop()
            
                if node.left is not None:
                    stacks2.append(node.left)
                if node.right is not None:
                    stacks2.append(node.right)
            stacks1.extend(stacks2)
            stacks2 = []
        return count

"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node, dep):
            if (node.left is None) and (node.right is None):
                return dep
            if (node.left is not None) and (node.right is None):
                return depth(node.left, dep+1)
            if (node.left is None) and (node.right is not None):
                return depth(node.right, dep+1)
            else:
                return max(depth(node.left, dep+1), depth(node.right, dep+1))
        if root is None:
            return 0
        return depth(root, 1)
"""
