# Time Complexity: O(N) - visit each node once.
# Space Complexity: O(H) - recursive call stack, where H is the tree height.
#                        - O(log N) for balanced trees, O(N) for skewed trees.

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal ans
            if not node:
                return 0 
            
            # get the max path sum from left and right subtrees (ignore negatives)
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            # update the global max path sum including this node
            ans = max(ans, left + right + node.val)
            
            # return the max path sum that can be extended to the parent
            return max(left, right) + node.val
        
         # initialize with the smallest possible value
        ans = float('-inf') 
        # start DFS from the root
        dfs(root)  
        return ans
