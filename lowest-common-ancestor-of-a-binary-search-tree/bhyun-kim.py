"""
235. Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
Solution:
    - If both p and q are greater than the root, the lowest common ancestor is in the right subtree.
    - If both p and q are less than the root, the lowest common ancestor is in the left subtree.
    - Otherwise, the root is the lowest common ancestor.

Time complexity: O(N)
    - The function is called recursively for each node
Space complexity: O(N)
    - Maximum depth of the recursion is the height of the tree
"""

class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        
        if p.val > root.val and q.val > root.val:    
            return self.lowestCommonAncestor(root.right, p, q)
    
        elif p.val < root.val and q.val < root.val:    
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root