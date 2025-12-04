# idea : DFS

# time : O(n)
# space : O(n)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # edge case 
        if not root:
            return 0 
        max_depth = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            max_depth = max(depth, max_depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return max_depth

# another way : Down-top : recursive
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         return 1 + max(
#         self.maxDepth(root.left),
#         self.maxDepth(root.right)
#         )







        