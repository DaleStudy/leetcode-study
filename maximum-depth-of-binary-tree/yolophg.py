# Time Complexity: O(N) - visit each node once.
# Space Complexity: O(H) - the recursion stack goes as deep as the height of the tree.
#                          - Worst case (skewed tree): O(N)
#                          - Best case (balanced tree): O(log N)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        # if there's no node, the depth is just 0.
        if not root:
            return 0
        
        # recursively get the depth of left and right subtrees
        # then add 1 for the current node
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
