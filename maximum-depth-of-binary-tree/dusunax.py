'''
# 104. Maximum Depth of Binary Tree

use DFS to find the maximum depth of the binary tree.

## A. if we use a helper function (not a good idea)
``` 
helper function explanation:
- store the max_depth in the nonlocal variable.(outside of the helper function)
- base case: if the node is None, update the max_depth and return.
- in the helper function, do recursive call for the left and right children of the node.
  - update the count for the depth of the tree.
- update the max_depth when the node is a leaf node's children.
```

## B. return the max_depth directly
👉 why helper function is not necessary?
recursion function can return the max_depth directly.  
remove side effect & non-local variable.

## TC is O(n)

visit each node once for checking if it is a leaf node's children.

## SC is O(h)

h for height of the tree
'''
class Solution:
    '''
    A. first approach with side effect
    '''
    def maxDepthWithHelper(self, root: Optional[TreeNode]) -> int: 
        max_depth = 0

        def helper(node, count):
            nonlocal max_depth 
            if node is None:
                max_depth = max(max_depth, count)
                return

            helper(node.left, count+1) 
            helper(node.right, count + 1)

        helper(root, max_depth)

        return max_depth
    
    '''
    B. return the max_depth directly.
    - more concise & readable
    - no side effect & non-local variable
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int: 
        if root is None:
            return 0
        
        left_count = self.maxDepth(root.left)
        right_count = self.maxDepth(root.right)

        return max(left_count, right_count) + 1
