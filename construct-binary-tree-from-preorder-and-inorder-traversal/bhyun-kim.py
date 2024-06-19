"""
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Solution
    To solve this problem, we can use a recursive approach. 
    We can use a helper function that takes the left and right index of the inorder array.
    The helper function will create a root node with the value of the current preorder index.
    Then, it will recursively call itself with the left and right index of the left and right subtree.

    - Create a dictionary that maps the value of the inorder array to its index.
    - Create a variable to keep track of the current preorder index.
    - Create a helper function that takes the left and right index of the inorder array.
    - In the helper function, if the left index is greater than the right index, return None.
    - Create a root node with the value of the current preorder index.
    - Increment the preorder index.
    - Recursively call the helper function with the left and right index of the left and right subtree.
    - Return the root node.

Time Complexity : O(n)
    - The helper function is called n times.
    - The dictionary lookup is O(1).

Space Complexity : O(n)
    - The dictionary has n elements.
    - The recursive call stack has n elements.
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

        self.preorder_index = 0

        def array_to_tree(left, right):
            if left > right:
                return None

            root_value = preorder[self.preorder_index]
            self.preorder_index += 1

            root = TreeNode(root_value)

            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        return array_to_tree(0, len(inorder) - 1)