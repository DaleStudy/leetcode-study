# 
# 100. Same Tree
# https://leetcode.com/problems/same-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Time Complexity: O(N)- it visits every node once
    #Space Complexity: O(H)- H is the height of the tree, which is the maximum depth of the recursion stack
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS approach
        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False 
            if node1.val != node2.val:
                return False 
            return dfs(node1.left,node2.left) and dfs(node1.right,node2.right)

        return dfs(p, q) 

        