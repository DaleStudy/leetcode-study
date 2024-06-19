"""
230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Solution:
    To solve this problem, we can use an in-order traversal of the binary search tree.
    We can create a helper function that performs an in-order traversal of the tree and returns a list of the elements in sorted order.
    Then, we can return the k-th element from the list.

Time complexity: O(n)
    - The in-order traversal visits each node once.
    - The list concatenation is O(n).

Space complexity: O(n)
    - The list of elements has n elements.
"""


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inOrderSearch(root)[k-1]

    def inOrderSearch(self, root):
        output = []
        if root: 
            output += self.inOrderSearch(root.left)
            output += [root.val]
            output += self.inOrderSearch(root.right)
        return output