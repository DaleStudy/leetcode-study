"""
572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/description/

Solution:
    This solution uses a depth-first search to find the subtree in the tree.
    We can use a recursive function to traverse the tree and compare the nodes.
    If the given node is identical to the subtree, we return True.
    Otherwise, we go to the left and right subtrees recursively.
    In this solution we use two helper functions: depth_first_search and is_identical.

    Depth-first search:
    1. Check if the root is None.
    2. Check if the root is identical to the subtree.
    3. Go to the left and right subtrees recursively.

    Is identical:
    1. Check if both nodes are None.
    2. Check if one of the nodes is None.
    3. Check if the values of the nodes are equal.
    4. Compare the left and right subtrees recursively.


Complexity analysis:
    Time complexity: O(n*m)
        Where n is the number of nodes in the tree and m is the number of nodes in the subtree.
        The depth-first search function has a time complexity of O(n).
        The is_identical function has a time complexity of O(m).
        Therefore, the overall time complexity is O(n*m).

    Space complexity: O(n)
        Where n is the number of nodes in the tree.
        The space complexity is O(n) because of the recursive calls to the depth_first_search function.
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def depth_first_search(root):
            if root is None:
                return False

            if is_identical(root, subRoot):
                return True

            return depth_first_search(root.left) or depth_first_search(root.right)

        def is_identical(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is not None and root2 is None:
                return False
            if root1 is None and root2 is not None:
                return False
            if root1.val == root2.val:
                return (
                    is_identical(root1.left, root2.left)
                    == is_identical(root1.right, root2.right)
                    == True
                )
            else:
                return False

        return depth_first_search(root)
