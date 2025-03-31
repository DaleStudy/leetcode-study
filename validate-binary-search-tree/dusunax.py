'''
# 98. Validate Binary Search Tree

check if is a valid BST.
- the left value is smaller than the current value
- the right value is greater than the current value

👉 all left and right subtrees must also valid continuously. 
so, we need to check the low & high bound recursively. (not only check current node & immediate children)

## base case
- if the node is None, return True (empty tree is valid BST)
- valid node value has range of left < node.val < right, if not, return False
- recursively check the left and right subtree, update the low & high.
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low = float('-inf'), high = float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root) 
