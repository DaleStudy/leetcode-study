# Time Complexity: O(log N) on average (for balanced BST), worst case O(N) (skewed tree).
# Space Complexity: O(1) - don't use extra space, just a few variables.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
         # start from the root
        node = root 

        while node:  
            if p.val > node.val and q.val > node.val:
                # both p and q are in the right subtree, so move right
                node = node.right  
            elif p.val < node.val and q.val < node.val:
                # both p and q are in the left subtree, so move left
                node = node.left  
            else:
                # found the split point where one is on the left and the other is on the right
                # or when we reach p or q directly (since a node can be its own ancestor)
                return node  

        return None
