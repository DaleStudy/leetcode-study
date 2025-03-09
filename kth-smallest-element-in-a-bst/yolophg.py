# Time Complexity: O(N) - visit each node once in an inorder traversal.
# Space Complexity: O(N) - store all node values in a list.

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if not node:
                return
            
            # go left (smaller values first)
            inorder(node.left) 
            # add the current node's value
            values.append(node.val)  
            # go right (larger values next)
            inorder(node.right) 

        values = []
        inorder(root)
        
        # get the k-th smallest element (1-based index)
        return values[k - 1]  
