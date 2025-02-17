'''
# 104. Maximum Depth of Binary Tree

use DFS to find the maximum depth of the binary tree.

``` 
helper function explanation:
- store the max_depth in the nonlocal variable.(outside of the helper function)
- base case: if the node is None, update the max_depth and return.
- in the helper function, do recursive call for the left and right children of the node.
  - update the count for the depth of the tree.
- update the max_depth when the node is a leaf node's children.
```

## TC is O(n)

visit each node once for checking if it is a leaf node's children.

## SC is O(h)

h for height of the tree
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: 
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
