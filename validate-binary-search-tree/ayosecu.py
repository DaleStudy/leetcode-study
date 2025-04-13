from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        - Time Complexity: O(n), n = The number of nodes
        - Space Complexity: O(H), H = The height of tree
            - Stack size of checkVal
            - H = logn, if the tree is balanced
            - H = n, if the tree is skewed
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def checkVal(node, min_val, max_val):
            if not node:
                return True
            
            if node.val >= max_val or node.val <= min_val:
                return False
            
            return checkVal(node.left, min_val, node.val) and checkVal(node.right, node.val, max_val)

        return checkVal(root, float("-inf"), float("inf"))

def doTest():
    sol = Solution()
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    result1 = sol.isValidBST(root1)
    print(f"TC 1 is Passed!" if result1 == True else f"TC 1 is Failed! - Expected: {True}, Result: {result1}")

    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)
    result2 = sol.isValidBST(root2)
    print(f"TC 2 is Passed!" if result2 == False else f"TC 2 is Failed! - Expected: {False}, Result: {result2}")

doTest()
