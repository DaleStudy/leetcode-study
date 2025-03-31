# Time Complexity: O(n) - visit every node once during the inorder traversal
# Space Complexity: O(n) - store all node values in an array during traversal

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # helper to do an inorder traversal and return a list of values
        def inorder(node):
            if not node:
                return []
            # in-order: left -> current -> right
            return inorder(node.left) + [node.val] + inorder(node.right)

        # get the in-order traversal of the tree
        arr = inorder(root)

        # if there are duplicates, it's not a valid BST
        if len(arr) != len(set(arr)):
            return False
        
        # if it's sorted in strictly increasing order, it's a valid BST
        return arr == sorted(arr)
